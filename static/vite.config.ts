import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import tailwindcss from '@tailwindcss/vite';
import path from 'path';

export default defineConfig({
  plugins: [
    vue(), 
    tailwindcss()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'resources/js')
    },
  },
  build: {
    outDir: 'public',
    manifest: false,
    rollupOptions: {
      input: 'resources/js/app.ts',
      output: {
        assetFileNames: '[name][extname]',
        chunkFileNames: '[name].js',
        entryFileNames: '[name].js',
      },
    },

  },
  server: {
    host: '127.0.0.1',
    port: 3000,
    hmr: {
      host: '127.0.0.1',
    },
  },
})