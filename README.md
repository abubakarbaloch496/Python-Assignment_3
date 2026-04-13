# Python-Assignment_3
Problem 1 
Write a program that asks for: 
1. Name (string) 
2. Age (integer) 
3. Entrance exam score (integer, 0–100) 
4. Family income (float, annual income in dollars) 
Then apply these rules in order: 
 
Step 1 – Basic eligibility 
• If age < 16 → print "Sorry, too young." and stop. 
• Else if exam score < 60 → print "Exam score too low." and stop. 
 
Step 2 – Income-based admission (only if age ≥ 16 and score ≥ 60) 
Use if-elif-else on family income: 
Income range				Decision
Less than $30,000			"Admitted with full scholarship" 
$30,000 – $79,999 			"Admitted with partial scholarship"  
$80,000 or more 			"Admitted without scholarship"
Step 3 – Output 
Print the name followed by the decision message. 
 
Examples 
Example 1 
Enter name: Ali 
Enter age: 17 
Enter exam score: 75 
Enter family income: 25000 
 
Ali, Admitted with full scholarship 
Example 2 
Income range Decision 
Less than $30,000 "Admitted with full scholarship" 
$30,000 – $79,999 "Admitted with partial scholarship" 
$80,000 or more "Admitted without scholarship" 
Enter name: Sara 
Enter age: 14 
Enter exam score: 88 
Enter family income: 50000 
 
Sara, Sorry, too young. 
Example 3 
Enter name: John 
Enter age: 18 
Enter exam score: 55 
Enter family income: 40000 
 
John, Exam score too low. 
Example 4 
Enter name: Maria 
Enter age: 20 
Enter exam score: 85 
Enter family income: 95000 
 
Maria, Admitted without scholarship 
Example 5 
Enter name: Tom 
Enter age: 19 
Enter exam score: 70 
Enter family income: 50000 
 
Tom, Admitted with partial scholarship 
 
 
 
 
Requirements Checklist 
• Use input() to get name, age, exam score, income. 
• Convert age and score to int, income to float. 
• Use if for age check. 
• Use elif for exam score check. 
• Use if-elif-else for income brackets. 
• Use proper indentation (4 spaces). 
• No syntax errors. 
 

Problem 2 
Write a Python program that: 
1. Asks the user for two numbers. 
2. Swaps their values. 
3. Prints the numbers before and after swapping. 
 
Requirements 
• Use two variables, e.g., a and b. 
• Get input from the user using input(). 
• Convert inputs to integers (or floats). 
• Swap the values 
• Print the original values and the swapped values clearly. 
 
Example Output 
Enter first number: 15 
Enter second number: 42 
Before swap: 
a = 15, b = 42 
 
After swap: 
a = 42, b = 1
