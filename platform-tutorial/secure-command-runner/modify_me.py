#!/usr/bin/env python3
import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 modify_me.py <text>")
        return

    user_input = sys.argv[1]
    command = f"echo Processed: {user_input}"
    os.system(command)

if __name__ == "__main__":
    main()
