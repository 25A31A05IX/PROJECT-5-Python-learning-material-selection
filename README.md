# Inclusive Learning-Material Selection Under Budget
# Python programming project

📌 Project Overview

The Inclusive Learning-Material Selection Under Budget project is designed to select the best combination of educational materials within a limited budget.

Each learning material has a specific cost and accessibility benefit. The system uses algorithms to identify the combination that provides the maximum total benefit without exceeding the available budget.

This project is implemented using Python.

🎯 Objectives

- Select learning materials within a given budget.
- Maximize accessibility benefits.
- Implement the 0/1 Knapsack problem using Dynamic Programming.
- Compare Dynamic Programming with a Greedy approach.
- Verify results using Brute Force.

🛠️ Technologies Used

- Programming Language: Python
- IDE: Visual Studio Code
- Concepts: Data Structures and Algorithms
- Algorithm: 0/1 Knapsack
- Techniques: Dynamic Programming, Greedy Algorithm, Brute Force

⚙️ Algorithms Implemented

1. Dynamic Programming

- Solves the 0/1 Knapsack problem.
- Finds the optimal combination of learning materials.
- Maximizes total accessibility benefit within the budget.

2. Greedy Algorithm

- Calculates the benefit-to-cost ratio.
- Selects materials based on the highest ratio.
- Used as a comparison approach.

3. Brute Force

- Checks all possible combinations.
- Finds the maximum achievable benefit.
- Verifies the Dynamic Programming result for small inputs.

📥 Input Details

The program accepts:

- Number of learning materials
- Material name
- Material cost
- Accessibility benefit
- Total available budget

📤 Sample Input

3
Braille Learning Kit
200
90
Audio Learning Resources
150
80
Accessible Learning Software
100
85
300

📊 Expected Results

Algorithm| Maximum Benefit
Dynamic Programming| 175
Greedy| 165
Brute Force| 175

Verification Status: PASSED

⏱️ Time and Space Complexity

Algorithm| Complexity
Dynamic Programming Time| O(n × W)
Dynamic Programming Space| O(n × W)
Greedy Time| O(n log n)
Brute Force Time| O(n × 2ⁿ)

Here, n represents the number of materials and W represents the budget.

▶️ How to Run the Project

1. Install Python on your system.
2. Download or clone this repository.
3. Open the project folder in Visual Studio Code.
4. Open the terminal.
5. Execute the following command:

python main.py

6. Enter the material details and budget.
7. View the algorithm results and comparison.

🌍 Applications

- Inclusive education resource planning
- Educational institutions
- Accessibility resource allocation
- Budget-based learning material selection

🚀 Future Enhancements

- Develop a graphical user interface.
- Integrate a database for storing material details.
- Add accessibility-based material categories.
- Generate detailed selection reports.
- Support larger datasets.

👥 Project Information

Project Title: Inclusive Learning-Material Selection Under Budget

Domain: Data Structures and Algorithms

Programming Language: Python

📌 Conclusion

This project demonstrates how Dynamic Programming can solve budget-based learning-material selection efficiently. It helps identify the optimal combination of educational resources while maximizing accessibility benefits and supporting inclusive education.

---

Thank You!
