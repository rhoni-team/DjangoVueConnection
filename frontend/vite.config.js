// DjangoVueConnection/frontend/vite.config.js

import path from "node:path";
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'


const INPUT_DIR = "./src";
// define this variable
const OUTPUT_DIR = "./static/dist";


// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      "@": path.resolve(INPUT_DIR),
    },
  },
  root: path.resolve(INPUT_DIR),
  base: "/static/",
  server: {
    origin: "http://localhost:3000",
    host: "localhost",
    port: 3000,
  },
  build: { // add build dictionary
    manifest: true,
    outDir: path.resolve(OUTPUT_DIR),
    rollupOptions: {
      input: {
        main: path.join(INPUT_DIR, "/main.js"),
      },
    },
  },
})
