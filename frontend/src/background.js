// backend.js

"use strict";

import { app, protocol, BrowserWindow, dialog, ipcMain } from "electron";
import { createProtocol } from "vue-cli-plugin-electron-builder/lib";
import installExtension, { VUEJS3_DEVTOOLS } from "electron-devtools-installer";
const isDevelopment = process.env.NODE_ENV !== "production";
import path from "path";

const __dirname = path.resolve(path.dirname(""));
let recordWidgetWindow;
let recordWidgetWindowIsExtended = false;

// Scheme must be registered before the app is ready
protocol.registerSchemesAsPrivileged([
  { scheme: "app", privileges: { secure: true, standard: true } },
]);

async function createWindow() {
  // Create the browser window.
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    autoHideMenuBar: true,
    webPreferences: {
      // Use pluginOptions.nodeIntegration, leave this alone
      // See nklayman.github.io/vue-cli-plugin-electron-builder/guide/security.html#node-integration for more info
      nodeIntegration: process.env.ELECTRON_NODE_INTEGRATION,
      contextIsolation: !process.env.ELECTRON_NODE_INTEGRATION,
      enableRemoteModule: true,
      preload: path.join(__dirname, "src/preload.js"),
    },
  });

  recordWidgetWindow = new BrowserWindow({
    // parent: win,
    width: 100,
    height: 500,
    x: 0,
    y: 0,
    alwaysOnTop: true,
    autoHideMenuBar: true,
    // frame: false,
    transparent: true,
    resizable: false,
    titleBarStyle: "hidden",
    visibleOnFullScreen: true,
    webPreferences: {
      preload: path.join(__dirname, "src/preload.js"),
      nodeIntegration: process.env.ELECTRON_NODE_INTEGRATION,
      contextIsolation: !process.env.ELECTRON_NODE_INTEGRATION,
      enableRemoteModule: true,
    },
  });

  recordWidgetWindow.setVisibleOnAllWorkspaces(true);
  recordWidgetWindow.setFullScreenable(false);
  recordWidgetWindow.setAlwaysOnTop(true, "screen-saver", 1);

  if (process.env.WEBPACK_DEV_SERVER_URL) {
    // Load the url of the dev server if in development mode
    await win.loadURL(`${process.env.WEBPACK_DEV_SERVER_URL}`);
    await recordWidgetWindow.loadURL(
      `${process.env.WEBPACK_DEV_SERVER_URL}record`
    );
    // recordWidgetWindow.webContents.insertCSS(
    //   "html, ::-webkit-scrollbar { overflow-y : hidden }"
    // );
    // recordWidgetWindow.webContents.insertCSS(
    //   "html, body {-webkit-app-region: drag;}"
    // );
    recordWidgetWindow.webContents.insertCSS(
      "html, button {-webkit-app-region: no-drag;}"
    );
    if (!process.env.IS_TEST) win.webContents.openDevTools();
  } else {
    createProtocol("app");
    // Load the index.html when not in development
    win.loadURL("app://./index.html");
    recordWidgetWindow.loadURL("app://./index.html#/record");
  }
}

ipcMain.on("select-folder", (event, message) => {
  console.log("Message reçu depuis SelectFolderPath:", message);
  const result = dialog
    .showOpenDialog({ properties: ["openDirectory", "multiSelections"] })
    .then((result) => {
      if (!result.canceled) {
        event.sender.send("select-folder", result.filePaths[0]);
      }
      console.log(result);
    });
});

// ipcMain.on("start-resize", (event) => {
//   if (!recordWidgetWindowIsExtended) {
//     recordWidgetWindowIsExtended = true;
//     recordWidgetWindow.setSize(80, 40, true);
//     console.log(recordWidgetWindow.getSize());
//   }
// });

// ipcMain.on("end-resize", () => {
//   if (recordWidgetWindowIsExtended) {
//     setTimeout(() => {
//       recordWidgetWindow.setSize(40, 40, true);
//       recordWidgetWindowIsExtended = false;
//     }, 300);
//     console.log(recordWidgetWindow.getSize());
//   }
// });

// Quit when all windows are closed.
app.on("window-all-closed", () => {
  // On macOS it is common for applications and their menu bar
  // to stay active until the user quits explicitly with Cmd + Q
  if (process.platform !== "darwin") {
    app.quit();
  }
});

app.on("activate", () => {
  // On macOS it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (BrowserWindow.getAllWindows().length === 0) createWindow();
  // createRecordWidgetWindow()
});

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.on("ready", async () => {
  if (isDevelopment && !process.env.IS_TEST) {
    // Install Vue Devtools
    try {
      await installExtension(VUEJS3_DEVTOOLS);
    } catch (e) {
      console.error("Vue Devtools failed to install:", e.toString());
    }
  }
  createWindow();
});

// Exit cleanly on request from parent process in development mode.
if (isDevelopment) {
  if (process.platform === "win32") {
    process.on("message", (data) => {
      if (data === "graceful-exit") {
        app.quit();
      }
    });
  } else {
    process.on("SIGTERM", () => {
      app.quit();
    });
  }
}
