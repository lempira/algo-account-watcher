import { useSuspenseQuery } from "@tanstack/react-query";
import { ACCOUNT_HISTORY_QUERY_KEY } from "../constants";
import NotificationTable from "./NotificationTable";
import { getAccountHistory } from "./api";

interface AccountHistoryProps {
  address: string;
  enableQuery: boolean;
}

const AccountHistory = ({ address, enableQuery }: AccountHistoryProps) => {
  const { data = [] } = useSuspenseQuery({
    queryKey: [...ACCOUNT_HISTORY_QUERY_KEY, address, enableQuery],
    queryFn: () => (enableQuery ? getAccountHistory(address) : null),
  });
  return (
    <div className="max-h-[500px]" style={{ overflow: "auto" }}>
      <NotificationTable data={data ?? []} />
    </div>
  );
};

export default AccountHistory;
