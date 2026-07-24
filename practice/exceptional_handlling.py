try:
    # 1. Run the risky code here
    result = 10 / 2
except ZeroDivisionError as e:
    # 2. Executes ONLY if a ZeroDivisionError occurs
    print(f"Error caught: {e}")
else:
    # 3. Executes ONLY if the try block succeeds without any errors
    print("Success! No errors occurred.")
finally:
    # 4. ALWAYS executes, no matter what happens (even if the code crashed or returned)
    print("Cleanup: This block runs absolute last.")
