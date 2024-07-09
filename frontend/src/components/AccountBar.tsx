import { useMutation, useQueryClient } from "@tanstack/react-query";
import { FaWallet } from "react-icons/fa";
import { MdDelete } from "react-icons/md";
import { ADDRESS_ENDPOINT, WATCHED_ADDRESSES_QUERY_KEY } from "../constants";
import { useState } from "react";
import { IoIosArrowForward } from "react-icons/io";
import AccountHistory from "./AccountHistory";
import { ComponentErrorSuspense } from "./ComponentErrorBoundary";

interface AccountBarProps {
  address: string;
  amount: number;
}

const AccountBar = ({ address, amount }: AccountBarProps) => {
  const queryClient = useQueryClient();
  const [openDetails, setOpenDetails] = useState(false);

  const mutateRemoveAddress = useMutation({
    mutationFn: async (address: string) => {
      const response = await fetch(`${ADDRESS_ENDPOINT}/${address}`, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
        },
      });

      if (!response.ok) {
        const errorResponse = await response.json();
        throw new Error(errorResponse.detail ?? "Something went wrong");
      }

      return response.json();
    },
  });

  const handleRemove = () => {
    mutateRemoveAddress.mutate(address, {
      onSuccess: () => {
        queryClient.invalidateQueries({
          queryKey: WATCHED_ADDRESSES_QUERY_KEY,
        });
      },
      onError: (error) => {
        // TODO: Handle error in UI
        console.log({ error });
      },
    });
  };

  const calculatedAmount = Math.round(amount / 10000) / 100;
  return (
    <div key={address} className="collapse bg-base-200">
      <input
        type="checkbox"
        className="hidden"
        checked={openDetails}
        onChange={() => null}
      />
      <div className="flex flex-col p-2">
        <div className="flex justify-between items-center">
          <div className="flex items-center">
            <button
              className="btn btn-link tooltip tooltip-right"
              data-tip="Show Account History"
              onClick={() => setOpenDetails(!openDetails)}
              aria-label="Show Account History"
            >
              <IoIosArrowForward
                className="h-[24px] w-[24px]"
                style={{
                  transition: "transform 0.15s linear",
                  transform: `rotate(${openDetails ? 90 : 0}deg)`,
                }}
              />
            </button>
            <FaWallet className="m-2" />
            <div className="collapse-title text-xl font-medium flex justify-between">
              {address}
            </div>
          </div>
          <button
            className="tooltip tooltip-left"
            data-tip="Stop Watching Address"
            aria-label="Stop Watching Address"
          >
            <MdDelete
              onClick={handleRemove}
              className="m-2 h-[24px] w-[24px]"
            />
          </button>
        </div>
        <div className="ml-2">Current Balance: {calculatedAmount} ALGOs</div>
      </div>
      <div className="collapse-content">
        <ComponentErrorSuspense errorMsg="Failed to account history">
          <AccountHistory address={address} enableQuery={openDetails} />
        </ComponentErrorSuspense>
      </div>
    </div>
  );
};

export default AccountBar;
