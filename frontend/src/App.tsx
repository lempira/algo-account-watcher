import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import AddressInput from "./components/AddressInput";
import Navbar from "./components/Navbar";
import WatchedAddresses from "./components/WatchedAddresses";
import { Suspense } from "react";
import RefreshAddresses from "./components/RefreshAddresses";
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
