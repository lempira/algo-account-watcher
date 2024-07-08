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
  };
};

export default getProxy;
