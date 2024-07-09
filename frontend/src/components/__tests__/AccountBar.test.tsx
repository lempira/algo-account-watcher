import { expect, test, vi, afterEach } from "vitest";
import { renderProvider } from "../../utils/test-utils";
import AccountBar from "../AccountBar";
import { userEvent } from "@testing-library/user-event";
import { screen, waitFor } from "@testing-library/react";
import { getAccountHistory } from "../api";
import { mockAccount, mockedNotifications } from "./testData";

vi.mock("../api");

afterEach(() => {
  vi.resetAllMocks();
});

test("Account Bar renders correctly", () => {
  const { address: mockAddress, amount: mockAmount } = mockAccount;
  renderProvider(<AccountBar address={mockAddress} amount={mockAmount} />);

  expect(screen.getByText(mockAddress)).toBeInTheDocument();
  expect(screen.getByText(new RegExp("Current Balance"))).toBeInTheDocument();
  expect(
    screen.getByRole("button", {
      name: /show account history/i,
    }),
  ).toBeInTheDocument();
  expect(
    screen.getByRole("button", {
      name: /stop watching address/i,
    }),
  ).toBeInTheDocument();
});

test("Account Bar expands correctly", async () => {
  const { address: mockAddress, amount: mockAmount } = mockAccount;
  const mockedAccountHistory = mockedNotifications.filter(
    (n) => n.address === mockAddress,
  );
  vi.mocked(getAccountHistory).mockResolvedValueOnce(mockedAccountHistory);
  const user = userEvent.setup();
  renderProvider(<AccountBar address={mockAddress} amount={mockAmount} />);

  const expandBtn = screen.getByRole("button", {
    name: /show account history/i,
  });
  await user.click(expandBtn);
  await waitFor(() => {
    expect(getAccountHistory).toHaveBeenCalledWith(mockAddress);
  });
  expect(
    await screen.findByText(mockedAccountHistory[0]?.previous_amount ?? 0),
  ).toBeInTheDocument();
});
