// backend.js

"use strict";

import { app, protocol, BrowserWindow, dialog, ipcMain } from "electron";
import { createProtocol } from "vue-cli-plugin-electron-builder/lib";
import installExtension, { VUEJS3_DEVTOOLS } from "electron-devtools-installer";
const isDevelopment = process.env.NODE_ENV !== "production";
import path from "path";

const __dirname = path.resolve(path.dirname(""));
let recordWidgetWindow;
let win;
let recordWidgetWindowIsExtended = false;

protocol.registerSchemesAsPrivileged([
  { scheme: "app", privileges: { secure: true, standard: true } },
]);

// CREATING WINDOWS

async function createWindow() {
  win = new BrowserWindow({
    width: 800,
    height: 600,
    autoHideMenuBar: true,
    webPreferences: {
      nodeIntegration: process.env.ELECTRON_NODE_INTEGRATION,
      contextIsolation: !process.env.ELECTRON_NODE_INTEGRATION,
      enableRemoteModule: true,
      preload: path.join(__dirname, "src/preload.js"),
    },
  });

  recordWidgetWindow = new BrowserWindow({
    width: 87,
    height: 40,
    x: 0,
    y: 0,
    alwaysOnTop: true,
    autoHideMenuBar: true,
    frame: false,
    transparent: true,
    // resizable: false,
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
    await win.loadURL(`${process.env.WEBPACK_DEV_SERVER_URL}`);
    await recordWidgetWindow.loadURL(
      `${process.env.WEBPACK_DEV_SERVER_URL}record`
    );
    recordWidgetWindow.webContents.insertCSS(
      "html, button {-webkit-app-region: no-drag;}"
    );
    if (!process.env.IS_TEST) win.webContents.openDevTools();
  } else {
    createProtocol("app");
    win.loadURL("app://./index.html");
    recordWidgetWindow.loadURL("app://./index.html#/record");
  }
}

// HANDLING IPC

ipcMain.on("update-libraries", () => {
  console.log("background.js: receiving update lib");
  recordWidgetWindow.webContents.send("libraries-updated");
});

ipcMain.on("update-bac_rec", () => {
  console.log("background.js: receiving update lib");
  recordWidgetWindow.webContents.send("bac_rec-updated");
});

ipcMain.on("select-folder-path", async (event, message) => {
  console.log("Message reçu depuis SelectFolderPath:", message);
  const result = dialog
    .showOpenDialog({ properties: ["openDirectory", "multiSelections"] })
    .then((result) => {
      if (!result.canceled) {
        const filePath = result.filePaths[0];
        console.log("select-folder:", filePath);
        try {
          event.sender.send("select-folder", filePath);
          recordWidgetWindow.webContents.send("libraries-updated");
        } catch (error) {
          console.error("Error adding library path:", error);
        }
      }
    });
});

ipcMain.on("start-resize", (event) => {
  if (!recordWidgetWindowIsExtended) {
    recordWidgetWindowIsExtended = true;
    recordWidgetWindow.setResizable(true);
    recordWidgetWindow.setSize(87, 60, true);
    recordWidgetWindow.setResizable(false);
  }
});

ipcMain.on("end-resize", () => {
  if (recordWidgetWindowIsExtended) {
    recordWidgetWindow.setResizable(true);
    recordWidgetWindow.setSize(87, 40, true);
    recordWidgetWindow.setResizable(false);
    recordWidgetWindowIsExtended = false;
  }
});

// Quit when all windows are closed.

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    app.quit();
  }
});

// LAUNCHING APP

app.on("activate", () => {
  if (BrowserWindow.getAllWindows().length === 0) createWindow();
});

app.on("ready", async () => {
  if (isDevelopment && !process.env.IS_TEST) {
    try {
      await installExtension(VUEJS3_DEVTOOLS);
    } catch (e) {
      console.error("Vue Devtools failed to install:", e.toString());
    }
  }
  createWindow();
});

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
