def knapsack(names, cost, benefit, budget):

    n = len(cost)

    dp = [[0 for _ in range(budget + 1)]
          for _ in range(n + 1)]

    # Build DP table
    for i in range(1, n + 1):

        for w in range(budget + 1):

            if cost[i - 1] <= w:

                dp[i][w] = max(
                    benefit[i - 1] +
                    dp[i - 1][w - cost[i - 1]],

                    dp[i - 1][w]
                )

            else:
                dp[i][w] = dp[i - 1][w]

    # Display selected materials
    print("\n===== DYNAMIC PROGRAMMING =====")
    print("Selected Learning Materials:")

    w = budget
    total_cost = 0

    for i in range(n, 0, -1):

        if dp[i][w] != dp[i - 1][w]:

            print(
                names[i - 1],
                "| Cost:", cost[i - 1],
                "| Benefit:", benefit[i - 1]
            )

            total_cost += cost[i - 1]
            w -= cost[i - 1]

    print("Total Cost:", total_cost)
    print("Maximum Accessibility Benefit:", dp[n][budget])

    return dp[n][budget]


# 2. Greedy Algorithm

def greedy(names, cost, benefit, budget):

    n = len(cost)

    # Calculate benefit-to-cost ratio
    items = sorted(
        range(n),
        key=lambda i: benefit[i] / cost[i],
        reverse=True
    )

    total_cost = 0
    total_benefit = 0

    print("\n===== GREEDY APPROACH =====")
    print("Selected Learning Materials:")

    for i in items:

        if cost[i] <= budget - total_cost:

            total_cost += cost[i]
            total_benefit += benefit[i]

            print(
                names[i],
                "| Cost:", cost[i],
                "| Benefit:", benefit[i]
            )

    print("Total Cost:", total_cost)
    print("Total Benefit:", total_benefit)

    return total_benefit


# 3. Brute Force Verification

def brute_force(cost, benefit, budget):

    n = len(cost)
    maximum_benefit = 0

    for mask in range(1 << n):

        total_cost = 0
        total_benefit = 0

        for i in range(n):

            if mask & (1 << i):

                total_cost += cost[i]
                total_benefit += benefit[i]

        if total_cost <= budget:

            maximum_benefit = max(
                maximum_benefit,
                total_benefit
            )

    return maximum_benefit


# 4. Main Program

def main():

    print("=" * 55)
    print(" INCLUSIVE LEARNING-MATERIAL SELECTION SYSTEM")
    print("=" * 55)

    try:

        n = int(input("Enter number of materials (1-20): "))

        if n <= 0 or n > 20:
            print("Invalid number! Enter between 1 and 20.")
            return

        names = []
        cost = []
        benefit = []

        # Input material details
        for i in range(n):

            print("\nMaterial", i + 1)

            name = input("Enter material name: ").strip()

            if not name:
                print("Material name cannot be empty!")
                return

            c = int(input("Enter cost: "))
            b = int(input("Enter accessibility benefit: "))

            if c <= 0 or b < 0:
                print("Invalid cost or benefit!")
                return

            names.append(name)
            cost.append(c)
            benefit.append(b)

        # Input budget
        budget = int(input("\nEnter total budget: "))

        if budget < 0 or budget > 100000:
            print("Budget must be between 0 and 100000.")
            return

        # Execute algorithms
        dp_result = knapsack(
            names, cost, benefit, budget
        )

        greedy_result = greedy(
            names, cost, benefit, budget
        )

        print("\n===== BRUTE FORCE VERIFICATION =====")

        brute_result = brute_force(
            cost, benefit, budget
        )

        print("Brute Force Maximum Benefit:", brute_result)

        if dp_result == brute_result:
            print("Verification Status: PASSED")
        else:
            print("Verification Status: FAILED")

        # Final comparison
        print("\n===== PROJECT COMPARISON =====")

        print("Dynamic Programming Benefit:", dp_result)
        print("Greedy Approach Benefit:", greedy_result)
        print("Brute Force Benefit:", brute_result)

        print("\nDP gives the optimal 0/1 Knapsack solution.")
        print("Greedy is used as a comparison heuristic.")

        # Complexity analysis
        print("\n===== COMPLEXITY ANALYSIS =====")

        print("DP Time Complexity: O(n * W)")
        print("DP Space Complexity: O(n * W)")
        print("Greedy Time Complexity: O(n log n)")
        print("Brute Force Time Complexity: O(n * 2^n)")

        print("\n" + "=" * 55)
        print(" PROJECT COMPLETED SUCCESSFULLY!")
        print("=" * 55)

    except ValueError:
        print("Invalid input! Please enter numbers correctly.")


# Program execution
if __name__ == "__main__":
    main()
