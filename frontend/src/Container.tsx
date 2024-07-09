import Navbar from "./components/Navbar";
import HelpText from "./components/HelpText";
import AddressInput from "./components/AddressInput";
import { ComponentErrorSuspense } from "./components/ComponentErrorBoundary";
import WatchedAddresses from "./components/WatchedAddresses";
import { testFn } from "./components/api";

const Container = () => {
  const asdf = testFn();
  console.log({ asdf, testFn });
  return (
    <div className="container mx-auto flex flex-col align-middle lg:p-4">
      <Navbar />
      <HelpText />
      <AddressInput />
      <div className="my-7" />
      <ComponentErrorSuspense errorMsg="Failed to load watched addresses">
        <WatchedAddresses />
      </ComponentErrorSuspense>
    </div>
  );
};

export default Container;
