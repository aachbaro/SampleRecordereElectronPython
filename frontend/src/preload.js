// frontend/src/preload.js

// const { contextBridge, ipcRenderer } = require('electron');

const { contextBridge, ipcRenderer } = require('electron')

// window.ipcRender = ipcRenderer

// Expose ipcRenderer to the client
contextBridge.exposeInMainWorld('ipcRenderer', {
  send: (channel, data) => {
    ipcRenderer.send(channel, data)
  },
  receive: (channel, func) => {
    ipcRenderer.on(channel, (event, ...args) => func(...args))
}
})
