import { defineConfig, loadEnv } from "vite";
import react from "@vitejs/plugin-react-swc";
import tsconfigPaths from "vite-tsconfig-paths";
import mkcert from "vite-plugin-mkcert";
import getProxy from "./src/scripts/setupProxy";

// https://vitejs.dev/config/
export default defineConfig(({ mode }) => {
  process.env = { ...process.env, ...loadEnv(mode, process.cwd()) };
  const { VITE_API_URL = "", VITE_APP_URL = "" } = process.env;

  return {
    plugins: [react(), tsconfigPaths(), mkcert()],
    server: {
      host: VITE_APP_URL,
      proxy: getProxy({ VITE_API_URL }),
    },
  };
});
