import {
  ColumnDef,
  flexRender,
  getCoreRowModel,
  getSortedRowModel,
  useReactTable,
} from "@tanstack/react-table";
import { useMemo } from "react";
import { AccountNotification } from "../types";

interface NotificationTableProps {
  data: AccountNotification[];
}
const NotificationTable = ({ data }: NotificationTableProps) => {
  const columns = useMemo<ColumnDef<AccountNotification, string>[]>(
    () => [
      {
        header: "Record Time",
        accessorKey: "created",
        cell: (info) => {
          const createdTime = info.getValue();
          return new Date(createdTime).toLocaleString();
        },
      },
      {
        header: "Previous Amount",
        accessorKey: "previous_amount",
        cell: (info) => info.getValue(),
      },
      {
        header: "New Amount",
        accessorKey: "current_amount",
        cell: (info) => info.getValue(),
      },
      {
        header: "Message",
        accessorKey: "message",
        cell: (info) => info.getValue(),
      },
    ],
    [],
  );

  const table = useReactTable({
    columns,
    data,
    debugTable: true,
    getCoreRowModel: getCoreRowModel(),
    getSortedRowModel: getSortedRowModel(),
  });
  return (
    <table className="table">
      <thead className="sticky top-0 bg-base-200">
        {table.getHeaderGroups().map((headerGroup) => (
          <tr key={headerGroup.id}>
            {headerGroup.headers.map((header) => {
              return (
                <th key={header.id} colSpan={header.colSpan}>
                  {header.isPlaceholder ? null : (
                    <div
                      className={
                        header.column.getCanSort()
                          ? "cursor-pointer select-none"
                          : ""
                      }
                      onClick={header.column.getToggleSortingHandler()}
                      title={
                        header.column.getCanSort()
                          ? header.column.getNextSortingOrder() === "asc"
                            ? "Sort ascending"
                            : header.column.getNextSortingOrder() === "desc"
                              ? "Sort descending"
                              : "Clear sort"
                          : undefined
                      }
                    >
                      {flexRender(
                        header.column.columnDef.header,
                        header.getContext(),
                      )}
                      {{
                        asc: " 🔼",
                        desc: " 🔽",
                      }[header.column.getIsSorted() as string] ?? null}
                    </div>
                  )}
                </th>
              );
            })}
          </tr>
        ))}
      </thead>
      <tbody>
        {table
          .getRowModel()
          .rows.slice(0, 100)
          .map((row) => {
            return (
              <tr key={row.id}>
                {row.getVisibleCells().map((cell) => {
                  return (
                    <td key={cell.id}>
                      {flexRender(
                        cell.column.columnDef.cell,
                        cell.getContext(),
                      )}
                    </td>
                  );
                })}
              </tr>
            );
          })}
      </tbody>
    </table>
  );
};

export default NotificationTable;
