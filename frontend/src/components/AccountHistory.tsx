import { useSuspenseQuery } from "@tanstack/react-query";
import { ACCOUNT_HISTORY_QUERY_KEY, NOTIFICATION_ENDPOINT } from "../constants";
import { AccountNotification } from "../types";
import NotificationTable from "./NotificationTable";

interface AccountHistoryProps {
  address: string;
  enableQuery: boolean;
}

const getAccountHistory = async (
  address: string
): Promise<AccountNotification[]> => {
  const response = await fetch(`${NOTIFICATION_ENDPOINT}/${address}`);
  return response.json();
};

const AccountHistory = ({ address, enableQuery }: AccountHistoryProps) => {
  const { data = [], error } = useSuspenseQuery({
    queryKey: [...ACCOUNT_HISTORY_QUERY_KEY, address, enableQuery],
    queryFn: () => (enableQuery ? getAccountHistory(address) : null),
  });
  console.log({ data, enableQuery });
  return (
    <div className="max-h-[500px]" style={{ overflow: "auto" }}>
      <NotificationTable data={data ?? []} />
    </div>
  );
};

export default AccountHistory;
