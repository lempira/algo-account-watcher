import { Account, AccountNotification } from "../../types";

const mockAddress1 = "test-address-1";
const mockAddress2 = "test-address-2";
const mockAmount = 123456789;

export const mockAccount: Account = {
  address: mockAddress1,
  amount: mockAmount,
};

export const mockedNotifications: AccountNotification[] = [
  {
    id: 1,
    address: mockAddress1,
    previous_amount: 500000000,
    current_amount: 750000000,
    message: "Amount Updated",
    created: "2023-10-01T10:00:00Z",
  },
  {
    id: 2,
    address: mockAddress1,
    previous_amount: 300000000,
    current_amount: 450000000,
    message: "Amount Updated",
    created: "2023-10-02T11:00:00Z",
  },
  {
    id: 3,
    address: mockAddress2,
    previous_amount: 1000000000,
    current_amount: 800000000,
    message: "Your account has been debited by $20.",
    created: "2023-10-03T12:00:00Z",
  },
  {
    id: 4,
    address: mockAddress2,
    previous_amount: 600000000,
    current_amount: 900000000,
    message: "Amount Updated",
    created: "2023-10-04T13:00:00Z",
  },
];
