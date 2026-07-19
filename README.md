🐍 Python Beginner Projects
12 hands-on projects with ready-to-use AI prompts, organized by difficulty.
📊 Difficulty Legend
Table
Badge	Level	Description
🟢 Easy	Beginner	Core Python basics: variables, loops, conditionals
🟡 Medium	Intermediate	Classes, file I/O, APIs, data structures
🔴 Hard	Advanced	Visualization, web frameworks, complex architectures
🗺️ Suggested Learning Path
Table
Week	Projects	Focus
1–2	1–5	Variables, loops, conditionals, basic file handling
3–4	6–10	Classes, APIs, data structures
5–6	11–12	Data visualization, complex architectures
📁 Projects
1. Number Guessing Game
Table
Difficulty	🟢 Easy
Tags	Loops, Conditionals, random
Description	The computer picks a random number, the user tries to guess it. Learn loops, conditionals, and the random module.
<details>
<summary>📝 Click to expand prompt</summary>
plain
Write a Python number guessing game where the computer picks a random number between 1 and 100. Give the user 7 attempts. After each guess, tell them if it's too high or too low. At the end, reveal the number and ask if they want to play again. Use functions to organize your code.
</details>
2. To-Do List CLI App
Table
Difficulty	🟢 Easy
Tags	Lists, Dictionaries, File I/O
Description	Build a command-line to-do list manager. Add, remove, mark complete, and view tasks. Great for learning lists, dictionaries, and file I/O.
<details>
<summary>📝 Click to expand prompt</summary>
plain
Create a Python CLI to-do list app. Features: add a task, mark task as done, delete a task, list all tasks with status indicators, save tasks to a JSON file so they persist between runs. Use a menu-driven interface (type a number to choose an action). Keep the code clean with helper functions.
</details>
3. Password Generator
Table
Difficulty	🟢 Easy
Tags	Strings, random/secrets, CLI
Description	Generate strong, random passwords with customizable length and character sets. Learn string manipulation and the secrets module.
<details>
<summary>📝 Click to expand prompt</summary>
plain
Build a Python password generator CLI tool. Ask the user for password length (8-128 chars) and which character sets to include: uppercase, lowercase, digits, special symbols. Generate a secure random password using the 'secrets' module. Ensure at least one character from each selected set is included. Print the password and offer to generate another.
</details>
4. Unit Converter
Table
Difficulty	🟢 Easy
Tags	Functions, Dictionaries, Input Validation
Description	Convert between units (length, weight, temperature, currency). Practice functions, dictionaries, and user input validation.
<details>
<summary>📝 Click to expand prompt</summary>
plain
Write a Python unit converter that supports: length (meters ↔ feet, km ↔ miles), weight (kg ↔ lbs, g ↔ oz), temperature (C ↔ F ↔ K), and currency (use a simple fixed exchange rate dict). Present a menu, ask for value and units, validate input, perform conversion, and display the result with 2 decimal places. Handle invalid inputs gracefully with try/except.
</details>
5. Rock Paper Scissors
Table
Difficulty	🟢 Easy
Tags	random, Conditionals, Score Tracking
Description	The classic game against the computer. Learn about random choices, score tracking, and best-of-N match logic.
<details>
<summary>📝 Click to expand prompt</summary>
plain
Create a Rock Paper Scissors game in Python. The user plays against the computer. Track wins, losses, and ties across a best-of-5 match. After each round, show both choices and the result. At match end, declare the winner and show the final scoreboard. Add a 'play again' option. Use an enum or constants for choices instead of raw strings.
</details>
6. Contact Book
Table
Difficulty	🟡 Medium
Tags	File I/O, JSON/CSV, Search
Description	A simple address book to store names, phone numbers, and emails. Search, add, edit, and delete contacts. CSV/JSON persistence.
<details>
<summary>📝 Click to expand prompt</summary>
plain
Build a Python contact book app. Each contact has: name, phone, email, and address. Features: add contact, search by name (partial match), edit contact, delete contact, list all contacts sorted alphabetically, export to CSV, import from CSV. Store data in a JSON file. Use a class-based design with a Contact class and a ContactBook class. Include input validation for phone and email formats.
</details>
7. Quiz App
Table
Difficulty	🟡 Medium
Tags	Classes, JSON, time module
Description	A multiple-choice quiz with scoring, timer, and categories. Learn about classes, JSON data, and time tracking.
<details>
<summary>📝 Click to expand prompt</summary>
plain
Create a Python quiz app. Load questions from a JSON file with categories (Science, History, Tech). Each question has 4 options and 1 correct answer. Show one question at a time, track score, enforce a 15-second timer per question using the 'time' module. At the end, show: total score, percentage, time taken, and a breakdown by category. Save high scores to a file. Use OOP with Question and Quiz classes.
</details>
8. Expense Tracker
Table
Difficulty	🟡 Medium
Tags	datetime, Data Structures, File I/O
Description	Track daily expenses with categories, budgets, and monthly summaries. Practice data structures and date handling.
<details>
<summary>📝 Click to expand prompt</summary>
plain
Build a Python expense tracker CLI. Features: add expense (amount, category, date, note), view expenses by date range or category, set monthly budget per category and show alerts when exceeded, generate a monthly summary with total spent and category breakdown, export monthly report to a text file. Store data in JSON. Use the 'datetime' module for date handling. Include a simple bar chart using ASCII art for category breakdown.
</details>
9. Web Scraper (Basic)
Table
Difficulty	🟡 Medium
Tags	requests, BeautifulSoup, HTML Parsing
Description	Scrape headlines or weather data from a website. Learn requests, BeautifulSoup basics, and data extraction.
<details>
<summary>📝 Click to expand prompt</summary>
plain
Write a Python web scraper using 'requests' and 'BeautifulSoup4'. Scrape the top 10 headlines from a news website (e.g., Hacker News or a simple blog). Extract: title, link, and points/votes. Save results to a CSV file. Add error handling for network issues and missing elements. Include a feature to filter headlines by a keyword. Print a nicely formatted table in the terminal using string formatting.
</details>
10. Weather Dashboard
Table
Difficulty	🟡 Medium
Tags	API, JSON, requests
Description	Fetch real-time weather data from a public API and display it. Learn API requests, JSON parsing, and data formatting.
<details>
<summary>📝 Click to expand prompt</summary>
plain
Create a Python weather dashboard using the Open-Meteo API (free, no key needed). Features: ask user for a city name (use a simple city-to-coordinates lookup dict for 20 major cities), fetch current weather (temperature, humidity, wind speed, weather condition), fetch a 3-day forecast, display results in a clean terminal format with emojis for weather conditions. Add a 'compare cities' feature that shows side-by-side weather for 2 cities. Cache results for 10 minutes to avoid redundant API calls.
</details>
11. Personal Finance Dashboard
Table
Difficulty	🔴 Hard
Tags	matplotlib, pandas, Data Visualization
Description	A more advanced finance tool with data visualization using matplotlib. Track income, expenses, and savings over time.
<details>
<summary>📝 Click to expand prompt</summary>
plain
Build a Python personal finance dashboard using matplotlib and pandas. Features: load transaction data from a CSV (date, amount, category, type: income/expense), calculate monthly net savings, plot: monthly income vs expenses line chart, expense breakdown pie chart, savings trend area chart, category-wise spending bar chart. Add a 'budget vs actual' comparison chart. Export all charts as PNG files. Use pandas for data manipulation and matplotlib with a clean, consistent style. Include a summary report printed to console with key metrics.
</details>
12. URL Shortener
Table
Difficulty	🔴 Hard
Tags	Hashing, File I/O, CLI + Optional Flask
Description	A simple URL shortener with a mapping database. Learn about hashing, data persistence, and basic web concepts.
<details>
<summary>📝 Click to expand prompt</summary>
plain
Create a Python URL shortener. Core features: accept a long URL and generate a short 6-character code using a hash function (or random string with collision check), store the mapping in a JSON file, provide a lookup function that returns the original URL from a short code, track click counts per URL, list all shortened URLs with their click stats. Bonus: add a simple Flask web interface with a form to submit URLs and a redirect endpoint. Validate URLs before shortening. Include a 'custom alias' option where users can specify their own short code.
</details>
🚀 How to Use These Prompts
Pick a project based on your current skill level.
Copy the prompt and paste it into your AI assistant or code editor.
Read the generated code carefully — don't just copy it blindly.
Modify it: change colors, add features, break it and fix it.
Push to GitHub and build your portfolio!
📦 Requirements Summary
Table
Project	Extra Libraries
1–8	None (stdlib only)
9	requests, beautifulsoup4
10	requests
11	matplotlib, pandas
12	flask (optional)
Happy coding! 🐍
