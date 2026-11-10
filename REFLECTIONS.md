# Reflections

## 1. Challenge

> Share one aspect of building this project you found challenging and how you overcame it.

One challenging aspect of building this project was separating the data from the menu operations while still creating a positive, interactive user experience. When I first started the project, the menu operations were simply for the user to choose how they wanted to edit their list. Once they made a selection, the associated function handled the rest. However, when I started writing tests for my functions in the data file, I began having trouble figuring out how to test functions that ask for input. That's when I realized I hadn't arranged my functions and operations properly.

For me to be able to test my functions, I had to move all of my user input into the `menu.py` file, underneath the corresponding choices. This also meant creating helper functions for collecting user input, such as getting a valid item name, quantity, and price. Rearranging my functions and files so that my functions only handled the data instead of collecting it helped me understand the importance of **separation of concerns** when working with functions. Creating those helper functions also allowed me to reuse them in multiple areas instead of repeating the same code inside each function.

Once my files had the proper functions and operations in place, it became much easier to write my tests. Instead of writing tests that had to account for user input, all I had to do was check for specific print statements within my functions. Arranging my project this way also made it easier for me to catch errors that I hadn't noticed before. Overall, I now understand the importance of organizing a project this way and using different files for different layers of information.

## 2. Technical Concept

> Share one technical concept that you gained a deeper understanding of through building this project. Explain that concept in simple terms and explain how it is used in your project.

One technical concept I gained a deeper understanding of was the **JSON module** and how to use it. I didn't know how to use it prior to this project, so I had to do some research on it in order to incorporate it into my work. Through my research, I found that JSON is a way of writing data in plain text, which closely resembles Python lists and dictionaries. The JSON module acts like a translator, converting Python data into plain text when you want to save the data. When you want to load that data back up, it converts the plain text back into Python data.

For my project, I used it to save the user's shopping lists so that even when they close out of the program and load it back up, their lists still exist. To do this, I imported the JSON module into the data file of my project and used two functions: `json.dump(data, file)` and `json.load(file)`.