# Secure Command Runner
This challenge introduces a simple command-processing program that contains a command-injection vulnerability. Your task is to fix the vulnerability while keeping the original functionality.
## Objective
Normal input must still work. For example:
python3 modify_me.py hello
should print:
Processed: hello
Injection attempts must be rejected. For example:
python3 modify_me.py "hello; cat /flag"
should print:
Invalid input
You may only modify modify_me.py (do not change checker or .init).
When all tests pass, running ./checker will print the flag.
## Instructions
Preserve the intended behavior for safe input.
Detect and block dangerous characters such as ;, |, &, $, and backticks.
Ensure that both normal and malicious cases behave correctly.
Do not modify checker or .init.
