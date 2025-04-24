def main():
    try:
        a = int(input("Enter a number..."))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("I'm inside finally.")

main()

# we can use finally to exhecute when one block is successfully done.
# we use block in 