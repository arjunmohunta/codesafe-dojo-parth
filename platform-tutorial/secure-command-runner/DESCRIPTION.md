# Bank Account Management System

## Objective
Implement a console-based bank account management system that allows users to create and manage bank accounts.

## Account Details
Each bank account has:
- Account Number (unique integer)
- Account Holder Name (string)
- Balance (float)
- Account Type (string)

## Functional Requirements
You must implement the following operations:

1. Add Account
   - Account number must be unique
   - Initial balance must be non-negative

2. Edit Account
   - Update account holder name
   - Update account type
   - Account must exist

3. Delete Account
   - Remove account permanently
   - Account must exist

4. Deposit Money
   - Amount must be positive
   - Account must exist

5. Withdraw Money
   - Amount must be positive
   - Balance must not go negative
   - Account must exist

6. Transfer Money
   - Both accounts must exist
   - Amount must be positive
   - Sender must have sufficient balance

7. Display Accounts
   - Show all stored accounts

## Constraints
- Do not use external libraries
- Store accounts in memory
- Follow object-oriented design
- Modify only the TODO (empty) methods

## Expected Skills
- Classes and objects
- Lists
- Control flow
- Input validation
