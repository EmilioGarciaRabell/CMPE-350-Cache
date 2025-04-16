# Creates a cache with mapping policy determined by user input

# prompt user to provide nominal size in Bytes
nominal_size = int(input("Enter nominal size in Bytes: "))

# prompt user to enter mapping policy
mapping_policy = input("Enter mapping policy (Direct Mapped or Fully Associative): ").strip().lower()