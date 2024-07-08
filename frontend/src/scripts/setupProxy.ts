import { CommonServerOptions } from "vite";

interface ProxyEnvVars {
  VITE_API_URL: string;
}

const getProxy = ({
  VITE_API_URL,
}: ProxyEnvVars): CommonServerOptions["proxy"] => {
  return {
    "/addresses": {
      target: `${VITE_API_URL}/addresses`,
      changeOrigin: true,
      rewrite: (path) => path.replace(/^\/addresses/, ""),
    },
    "/notifications": {
      target: `${VITE_API_URL}/notifications`,
      changeOrigin: true,
      rewrite: (path) => path.replace(/^\/notifications/, ""),
    },
  };
};

export default getProxy;
