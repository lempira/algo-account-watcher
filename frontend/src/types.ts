export interface Account {
  address: string;
  amount: number;
}

export interface AccountNotification {
  id: number;
  address: string;
  previous_amount: number;
  current_amount: number;
  message: string;
  created: string;
}
