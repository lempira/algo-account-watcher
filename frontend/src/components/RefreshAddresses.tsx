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
      <p className="text-2xl">Watched Addresses</p>
      <button
        className="btn btn-ghost tooltip tooltip-right"
        data-tip="Refresh Watched Addresses"
      >
        <IoIosRefresh
          onClick={refreshAddresses}
          className="h-[24px] w-[24px]"
        />
      </button>
      {showText && <p className="text-accent">Updated Available</p>}
    </div>
  );
};

export default RefreshAddresses;
