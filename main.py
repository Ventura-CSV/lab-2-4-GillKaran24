def main():
    original_str = "Python Programming"

    # Extract "Python" from the original string with index slicing
    sub1 = original_str[:6]

    # Extract "Programming" from the original string with index slicing
    sub2 = original_str[7:]

    # Merge two substrings using string concatenation
    merged_str = sub2 + " " + sub1

    print(sub2)
    print(sub1)
    print(merged_str)

    # Do not delete the return statement
    return sub2, sub1, merged_str

if __name__ == '__main__':
    main()
