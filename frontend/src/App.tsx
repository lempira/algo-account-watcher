import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import AddressInput from "./components/AddressInput";
import Navbar from "./components/Navbar";
import WatchedAddresses from "./components/WatchedAddresses";
import HelpText from "./components/HelpText";
import { ReactQueryDevtools } from "@tanstack/react-query-devtools";
import { ComponentErrorSuspense } from "./components/ComponentErrorBoundary";

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <div className="container mx-auto flex flex-col align-middle p-4">
        <Navbar />
        <HelpText />
        <AddressInput />
        <div className="my-7" />
        
        <ComponentErrorSuspense errorMsg="Failed to load watched addresses">
          <WatchedAddresses />
        </ComponentErrorSuspense>
      </div>
      <ReactQueryDevtools initialIsOpen={false} />
    </QueryClientProvider>
  );
}

export default App;
