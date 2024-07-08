import { useQueryClient } from "@tanstack/react-query";
import { IoIosRefresh } from "react-icons/io";
import { WATCHED_ADDRESSES_QUERY_KEY } from "./constants";

const RefreshAddresses = () => {
  const queryClient = useQueryClient();

  const refreshAddresses = () => {
    queryClient.invalidateQueries({
      queryKey: WATCHED_ADDRESSES_QUERY_KEY,
    });
  };

  return (
    <div className="flex justify-between">
      <p className="text-2xl">Watched Addresses</p>
      <button
        className="btn btn-ghost tooltip tooltip-left"
        data-tip="Refresh Watched Addresses"
      >
        <IoIosRefresh
          onClick={refreshAddresses}
          className="h-[24px] w-[24px]"
        />
      </button>
    </div>
  );
};

export default RefreshAddresses;
