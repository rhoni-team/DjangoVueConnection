import path from "node:path"; // add this import
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'


// define this variables
const INPUT_DIR = "./src";


// https://vitejs.dev/config/
export default defineConfig({
 plugins: [
   vue(),
 ],
 resolve: { // change the resolve.alias
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
})
