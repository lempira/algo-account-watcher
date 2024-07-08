import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import AddressInput from "./AddressInput";
import Navbar from "./Navbar";
import WatchedAddresses from "./WatchedAddresses";
import { Suspense } from "react";
import RefreshAddresses from "./RefreshAddresses";
const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <div className="container mx-auto flex flex-col align-middle">
        <Navbar />
        <AddressInput />
        <div className="my-7" />
        <RefreshAddresses />
        <Suspense
          fallback={<span className="loading loading-dots loading-lg"></span>}
        >
          <WatchedAddresses />
        </Suspense>
      </div>
    </QueryClientProvider>
  );
}

export default App;
