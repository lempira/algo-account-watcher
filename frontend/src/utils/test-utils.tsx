import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { render } from "@testing-library/react";
import { afterEach } from "vitest";

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      retry: false,
    },
  },
});

// Reset the queryClient between tests to clear the cache.
afterEach(() => {
  queryClient.clear();
});

export const renderProvider = (children: React.ReactNode) =>
  render(
    <QueryClientProvider client={new QueryClient()}>
      {children}
    </QueryClientProvider>,
  );
