import { ADDRESS_ENDPOINT, NOTIFICATION_ENDPOINT } from "../constants";
import { Account, AccountNotification } from "../types";

export const getWatchedAddresses = async (): Promise<Account[]> => {
  const response = await fetch(`${ADDRESS_ENDPOINT}/all`);
  return response.json();
};

export const getAccountHistory = async (
  address: string,
): Promise<AccountNotification[]> => {
  const response = await fetch(`${NOTIFICATION_ENDPOINT}/${address}`);
  return response.json();
};

export const testFn = () => {
  return 2;
};
