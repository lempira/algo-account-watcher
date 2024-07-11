import { describe, test, expect, afterEach, vi, beforeEach } from "vitest";
import { screen } from "@testing-library/react";
import RefreshAddresses from "../RefreshAddresses";
import { renderProvider } from "../../utils/test-utils";
import userEvent from "@testing-library/user-event";

vi.mock("../api");

afterEach(() => {
  vi.resetAllMocks();
});

describe("RefreshAddresses Component", () => {
  beforeEach(() => {
    renderProvider(<RefreshAddresses />);
  });

  test("should render correctly", () => {
    expect(screen.getByText(/Watched Addresses/i)).toBeInTheDocument();
    expect(
      screen.getByRole("button", { name: /Refresh Watched Addresses/i })
    ).toBeInTheDocument();
    expect(
      screen.queryByText(new RegExp("Updated Available", "i"))
    ).not.toBeInTheDocument();
  });

  test("should display tooltip text when hovered over refresh button", async () => {
    const user = userEvent.setup();
    const refreshButton = screen.getByRole("button", {
      name: /Refresh Watched Addresses/i,
    });
    await user.hover(refreshButton);
    expect(refreshButton).toHaveAttribute(
      "data-tip",
      "Refresh Watched Addresses"
    );
  });

  test('should show "Update Available" text after 60 seconds of clicking refresh icon', async () => {
    vi.useFakeTimers({
      shouldAdvanceTime: true,
    });
    const user = userEvent.setup();
    const refreshButton = screen.getByRole("button", {
      name: /Refresh Watched Addresses/i,
    });

    await user.click(refreshButton);
    await user.click(refreshButton);

    // Fast-forward 65 seconds
    vi.advanceTimersByTime(65000);

    expect(await screen.findByText(/Update Available/i)).toBeInTheDocument();

    vi.useRealTimers();
  });
});
