import { useQueryClient } from "@tanstack/react-query";
import { IoIosRefresh } from "react-icons/io";
import { WATCHED_ADDRESSES_QUERY_KEY } from "../constants";
import { useEffect, useState } from "react";

const RefreshAddresses = () => {
  const queryClient = useQueryClient();
  const [counter, setCounter] = useState(0);
  const [showText, setShowText] = useState(false);

  const refreshAddresses = () => {
    setCounter((prev) => prev + 1);
    queryClient.invalidateQueries({
      queryKey: WATCHED_ADDRESSES_QUERY_KEY,
    });
  };

  useEffect(() => {
    setShowText(false);
    const timer = setTimeout(() => {
      setShowText(true);
    }, 60000);
    return () => clearTimeout(timer);
  }, [counter]);

  return (
    <div className="flex items-center gap-2">
      <p className="lg:text-2xl ml-4">Watched Addresses</p>
      <button
        className="btn btn-ghost lg:tooltip tooltip-right"
        data-tip="Refresh Watched Addresses"
        aria-label="Refresh Watched Addresses"
        onClick={refreshAddresses}
      >
        <IoIosRefresh className="h-[20px] w-[20px] lg:h-[24px] lg:w-[24px]" />
      </button>
      {showText && (
        <p className="text-accent text-sm lg:text-base">Update Available</p>
      )}
    </div>
  );
};

export default RefreshAddresses;
