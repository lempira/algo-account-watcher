import { useSuspenseQuery } from "@tanstack/react-query";
import { WATCHED_ADDRESSES_QUERY_KEY } from "../constants";
import AccountBar from "./AccountBar";
import RefreshAddresses from "./RefreshAddresses";
import { getWatchedAddresses } from "./api";

const WatchedAddresses = () => {
  const { data = [], error } = useSuspenseQuery({
    queryKey: WATCHED_ADDRESSES_QUERY_KEY,
    queryFn: getWatchedAddresses,
  });

  return (
    <>
      {data.length > 0 ? (
        <>
          <RefreshAddresses />
          <div className="p-4">
            {error ? (
              <div role="alert" className="alert alert-error p-4">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-6 w-6 shrink-0 stroke-current"
                  fill="none"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
                  />
                </svg>
                <span>
                  Fetching watched addressed failed with the following message:{" "}
                  {error.message}
                </span>
              </div>
            ) : (
              <div className="p-4 flex flex-col gap-3">
                {data?.map((d) => (
                  <AccountBar
                    key={d.address}
                    address={d.address}
                    amount={d.amount}
                  />
                ))}
              </div>
            )}
          </div>
        </>
      ) : (
        <p className="p-4 text-center text-2xl italic">
          No watched addresses found. Add an address to start watching.
        </p>
      )}
    </>
  );
};

export default WatchedAddresses;
