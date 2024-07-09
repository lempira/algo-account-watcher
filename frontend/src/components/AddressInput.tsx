import { useMutation, useQueryClient } from "@tanstack/react-query";
import { useState } from "react";
import { ADDRESS_ENDPOINT, WATCHED_ADDRESSES_QUERY_KEY } from "../constants";

const AddressInput = () => {
  const [error, setError] = useState<Error | null>(null);
  const queryClient = useQueryClient();
  const mutateAddAddress = useMutation({
    mutationFn: async (address: string) => {
      const response = await fetch(`${ADDRESS_ENDPOINT}/add`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ address }),
      });

      if (!response.ok) {
        const errorResponse = await response.json();
        throw new Error(errorResponse.detail ?? "Something went wrong");
      }

      return response.json();
    },
  });

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const { currentTarget: form } = e;
    const formData = new FormData(form);
    const address = formData.get("address") as string;

    setError(null);
    mutateAddAddress.mutate(address, {
      onSuccess: () => {
        form.reset();
        queryClient.invalidateQueries({
          queryKey: WATCHED_ADDRESSES_QUERY_KEY,
        });
      },
      onError: (error) => {
        setError(error);
        form.reset();
      },
    });
  };

  return (
    <div className="w-full flex flex-col gap-2 self-center p-4">
      <form onSubmit={handleSubmit} className="flex gap-2 justify-center">
        <div className="w-full flex gap-2">
          <input
            type="text"
            name="address"
            placeholder="Algorand Account Address"
            className="input input-bordered flex-1"
          />
          <button
            type="submit"
            className="inline-block cursor-pointer rounded-md bg-gray-800 px-4 py-3 text-center text-sm font-semibold uppercase text-white transition duration-200 ease-in-out hover:bg-gray-900"
          >
            {mutateAddAddress.isPending ? (
              <span className="loading loading-spinner loading-md"></span>
            ) : (
              "Add"
            )}
          </button>
        </div>
      </form>
      {error && (
        <div
          role="alert"
          className="alert alert-error flex-1 flex justify-between"
        >
          <label>{error.message}</label>
          <button onClick={() => setError(null)}>
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
          </button>
        </div>
      )}
    </div>
  );
};

export default AddressInput;
