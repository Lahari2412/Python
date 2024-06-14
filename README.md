# Python 

# **Table Contents**

- [Overview of Python](#Overview-of-Python)

  - [What is Python?](#What-is-Python?)
  - [History of Python](#History-of-Python)
  - [Features of Python](#Features-of-Python)
  - [Installation and Setup](#Installation-and-Setup)
  - [Installing Python](#Installing-Python)
  - [Setting up the environment (IDLE, VS Code, Jupyter Notebook)](#Setting-up-the-environment)


-	[Python Syntax and Basics](#Python-Syntax-and-Basics)

  - [Writing and Executing Python Programs](#Writing-and-Executing-Python-Programs)	
  - [Python IDEs and Code Editors](#Python-IDEs-and-Code-Editors)
  - [Comments](#Comments)
  - [Variables and Data Types](#Variables-and-Data-Types)
  - [Basic Input/Output](#Basic-Input/Output])


- [Control Structures](#Control-Structures)

  - [Conditional Statements (if, elif, else)](#Conditional-Statements)
  - [Looping (for, while)](#Looping)
  - [List Comprehensions](#List-Comprehensions)


- [Data Structures](#Data-Structures)

  - [Lists](#Lists)
  - [Tuples](#uples)
  - [Sets](#Sets)
  - [Dictionaries](#Dictionaries)
  - [Strings and String Operations](#Strings-and-String-Operations)


- [Functions and Modules](#Functions-and-Modules)

  - [Defining Functions](#Defining-Functions)
  - [Function Arguments and Return Values](#Function-Arguments-and-Return-Values)
  - [Lambda Functions](#Lambda-Functions)
  - [Built-in Functions](#Built-in-Functions)
  - [Importing Modules and Packages](#Importing-Modules-and-Packages)
  - [Creating and Using Custom Modules](#Creating-and-Using-Custom-Modules)


- [File Handling](#File-Handling)

  - [Reading and Writing Files](#Reading-and-Writing-Files)
  - [Working with CSV Files](#Working-with-CSV-Files)
  - [File Operations](#File-Operations)


- [Object-Oriented Programming (OOP)](#Object-Oriented-Programming-(OOP))

  - [Classes and Objects](#Classes-and-Objects)
  - [Methods](#Methods)
  - [Inheritance](#Inheritance)
  - [Polymorphism](#Polymorphism)
  - [Encapsulation and Abstraction](#Encapsulation-and-Abstraction)


- [Error and Exception Handling](#Error-and-Exception-Handling)

  - [Understanding Errors and Exceptions](#Understanding-Errors-and-Exceptions)
  - [Try, Except, Finally](#Try-Except-Finally)
  - [Custom Exceptions](#Custom-Exceptions)


- [Working with Libraries](#Working-with-Libraries)

  - [NumPy for Numerical Computations](#NumPy-for-Numerical-Computations)
  - [Pandas for Data Analysis](#Pandas-for-Data-Analysis)
  - [Matplotlib and Seaborn for Data Visualization](#Matplotlib-and-Seaborn-for-Data-Visualization)
  - [Requests for HTTP Requests](#Requests-for-HTTP-Requests)


- [Regular Expressions](#Regular-Expressions)

  - [Introduction to Regular Expressions](#Introduction-to-Regular-Expressions)
  - [Using the re Module](#Using-the-re-Module)
  - [Pattern Matching and Substitution](#Pattern-Matching-and-Substitution)


- [Advanced Data Structures](#Advanced-Data-Structures)

  - [Collections Module](#Collections-Module)
  - [Defaultdict, Counter, and OrderedDict](#Defaultdict-Counter-and-OrderedDict)
  - [Heaps and Queues](#Heaps-and-Queues)


- [Iterators and Generators](#Iterators-and-Generators)

  - [Understanding Iterators](#Understanding-Iterators)
  - [Creating Generators](#Creating-Generators)
  - [Using yield](#Using-yield)
  - [Generator Expressions](#Generator-Expressions)

- [Decorators and Context Managers](#Decorators-and-Context-Managers)

  - [Understanding Decorators](#Understanding-Decorators)
  - [Writing Custom Decorators](#Writing-Custom-Decorators)
  - [Using with Statements](#Using-with-Statements)
  - [Creating Custom Context Managers](#Creating-Custom-Context-Managers)


- [Concurrency and Parallelism](#Concurrency-and-Parallelism)

  - [Threading](#Threading)
  - [Multiprocessing](#Multiprocessing)
  - [Asyncio for Asynchronous Programming](#Asyncio-for-Asynchronous-Programming)


- [Networking](#Networking)

  - [Sockets Programming](#Sockets-Programming)
  - [Web Scraping with BeautifulSoup](#Web-Scraping-with-BeautifulSoup)
  - [Building APIs with Flask/Django](#Building-APIs-with-Flask/Django)


- [Database Interaction](#Database-Interaction)

  - [Working with SQLite](#Working-with-SQLite)
  - [Using SQLAlchemy](#Using-SQLAlchemy)
  - [Connecting to MySQL/PostgreSQL](#Connecting-to-MySQL/PostgreSQL)


- [Testing and Debugging](#Testing-and-Debugging)

  - [Unit Testing with unittest](#Unit-Testing-with-unittest)
  - [Using pytest](#Using-pytest)
  - [Debugging with pdb](#Debugging-with-pdb)



## Overview of Python

### What is Python?
-------------------------

Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together.Python supports modules and packages, which encourages program modularity and code reuse.The major focus behind creating it is making it easier for developers to read and understand, also reducing the lines of code.

### History of Python
-----------------------------------

Python was created in 1980s by Guido van Rossum. During his research at the National Research Institute for Mathematics and Computer Science in the Netherlands, he created Python – a super easy programming language in terms of reading and usage. The first ever version was released in the year 1991 which had only a few built-in data types and basic functionality. 

Later, when it gained popularity among scientists for numerical computations and data analysis, in 1994, Python 1.0 was released with extra features like map, lambda, and filter functions. After that adding new functionalities and releasing newer versions of Python came into fashion. 

Python 1.5 released in 1997
Python 2.0 released in 2000
Python 3.0 in 2008 brought newer functionalities
The latest version of Python, Python 3.11 was released in 2022.

Newer functionalities being added to Python makes it more beneficial for developers and improved its performance. In recent years, Python has gained a lot of popularity and is a highly demanding programming language. It has spread its demand in various fields which includes machine learning, artificial intelligence, data analysis, web development, and many more giving you a high-paying job.

### Features of Python
----------------------------------

Python is a popular, high-level programming language known for its simplicity, readability, and versatility. Here are some key features of Python:

-  **Readability and Simplicity**:
    Python syntax is clear and easy to understand, making it an excellent choice for beginners.
    Emphasizes readability, reducing the cost of program maintenance.

-  **Interpreted Language**:
   Python code is executed line by line, making debugging easier.
   No need for compilation, which speeds up the development process.

-  **Dynamically Typed**:
   Variables in Python do not need explicit declaration to reserve memory space. The declaration happens automatically when a value is assigned.

-  **High-Level Language**:
   Python abstracts many complex details of the computer’s hardware, making it easier to focus on programming.

-  **Extensive Standard Library**:
   Python comes with a vast standard library, providing tools suited for many tasks including string operations, web service tools, and operating system interfaces.

-  **Cross-Platform Compatibility**:
   Python is compatible with various operating systems such as Windows, macOS, and Linux, allowing for cross-platform development.

- **Object-Oriented Programming (OOP)**:
   - Supports OOP which allows for the encapsulation of code within objects, promoting reuse and modularity.

- **Large Ecosystem and Libraries**:
   Python has a large ecosystem of third-party libraries and frameworks like NumPy, Pandas, Django, Flask, and TensorFlow, extending its capabilities.

- **Community Support**:
   Python has a large and active community, which contributes to a wealth of resources, tutorials, and libraries.

- **Integrated Development Environments (IDEs)**:
   There are several IDEs that support Python, such as PyCharm, VSCode, and Jupyter Notebook, which enhance development productivity.

- **Functional Programming Support**:
   Python supports functional programming features like higher-order functions, lambda functions, and list comprehensions.

- **Concurrency Support**:
  Python supports concurrent programming through threading, asyncio, and multiprocessing modules, making it possible to write efficient and parallel code.

- **Extensibility**:
  Python can be extended with modules written in C or C++.
  It can also be embedded within C/C++ programs to provide scripting capabilities.

- **Garbage Collection**:
   Python has built-in garbage collection to manage memory automatically, which helps in avoiding memory leaks.

- **Scripting and Automation**:
   Python is widely used for scripting and automation of repetitive tasks due to its simplicity and efficiency.

These features make Python a versatile and powerful tool for a wide range of applications, from web development and data analysis to artificial intelligence and scientific computing.



### Python Installation and Setup
---------------------------

#### Installing Python
---------------------

**Step 1: Download Python**

1. Go to the official Python website: [python.org](https://www.python.org/).
2. Navigate to the "Downloads" section.
3. Select the appropriate version for your operating system (Windows, macOS, or Linux).

**Step 2: Install Python**

**For Windows**:

1. Run the downloaded installer.
2. Ensure you check the box that says "Add Python to PATH".
3. Click "Install Now".
4. Follow the prompts to complete the installation.

**For macOS:**

1. Open the downloaded `.pkg` file.
2. Follow the instructions in the installer.

**For Linux:**

1. Open a terminal.
2. Use the package manager of your distribution to install Python. For example, on Ubuntu, you can use:
   ```sh
   sudo apt update
   sudo apt install python3
   ```

**Step 3: Verify the Installation**

Open a terminal or command prompt and type:
```sh
python --version
```
or

```sh
python3 --version
```
You should see the version of Python you installed.

**Step 4: Install a Code Editor or IDE**

While you can write Python code in any text editor, it's recommended to use an Integrated Development Environment (IDE) or a code editor that supports Python well. Some popular options include:

- **PyCharm**: A powerful IDE for Python development.
- **Visual Studio Code (VS Code)**: A lightweight but powerful source code editor with support for Python through extensions.
- **Jupyter Notebook**: An open-source web application that allows you to create and share documents that contain live code, equations, visualizations, and narrative text.

**Step 5: Install Necessary Packages**

Python uses packages to extend its functionality. The most common way to manage packages is with `pip`, which is included by default with Python installations. To install a package, use the following command:

```sh
pip install package_name
```

For example, to install the popular requests package, you would use:

```sh
pip install requests
```

**Step 6: Setting Up a Virtual Environment (Optional)**

Using virtual environments is a good practice to manage dependencies for different projects. To create a virtual environment:

1. Open a terminal or command prompt.
2. Navigate to your project directory.
3. Create a virtual environment using:

  > ```sh
  > python -m venv env
  > ```
   This will create a directory named `env` containing the virtual environment.
4. Activate the virtual environment:
   - **Windows**: `.\env\Scripts\activate`
   - **macOS and Linux**: `source env/bin/activate`
5. To deactivate the virtual environment, simply type:
   ```sh
   deactivate
   ```

**Step 7: Write Your First Python Script**

Create a new Python file, for example `hello.py`, and add the following code:
```python
print("Hello, World!")
```
Run the script by navigating to the directory containing the file and executing:
```sh
python hello.py
```

#### 	Setting up the environment (IDLE, VS Code, Jupyter Notebook)
-----------------------------------------------------

Setting up a development environment for Python involves choosing the right tools for your workflow. Below are detailed steps for setting up Python environments with IDLE, Visual Studio Code (VS Code), and Jupyter Notebook.

##### IDLE

IDLE (Integrated Development and Learning Environment) is the default editor that comes with Python. It’s simple to use and is a good starting point for beginners.

1. **Open IDLE**:
   - If you have installed Python, IDLE should already be installed.
   - Search for "IDLE" in your applications or open it from the terminal/command prompt by typing `idle`.

2. **Using IDLE**:
   - You can start coding directly in the Python shell that opens or create a new file (File -> New File) to write scripts.
   - Save your script with a `.py` extension.
   - Run your script by pressing `F5` or selecting Run -> Run Module from the menu.

##### Visual Studio Code (VS Code)

VS Code is a popular, open-source code editor with powerful features for Python development.

1. **Download and Install VS Code**:
   - Go to the [VS Code download page](https://code.visualstudio.com/Download).
   - Download and install the version for your operating system.

2. **Install the Python Extension**:
   - Open VS Code.
   - Go to the Extensions view by clicking the Extensions icon in the Activity Bar on the side of the window or by pressing `Ctrl+Shift+X`.
   - Search for "Python" and install the extension provided by Microsoft.

3. **Set Up a Python Workspace**:
   - Open the folder containing your Python project (File -> Open Folder).
   - Create a new Python file (`.py` extension) and start writing your code.

4. **Configure the Python Interpreter**:
   - Open the Command Palette (`Ctrl+Shift+P`).
   - Type `Python: Select Interpreter` and select the Python interpreter you want to use.

5. **Running Code**:
   - You can run your Python script by pressing `F5` or by right-clicking in the editor and selecting `Run Python File in Terminal`.

##### Jupyter Notebook

Jupyter Notebook is an open-source web application that allows you to create and share documents with live code, equations, visualizations, and narrative text.

1. **Install Jupyter Notebook**:
   - Open a terminal or command prompt.
   - If you don’t have `pip` installed, install it using:
     ```sh
     python -m ensurepip --upgrade
     ```
   - Install Jupyter using `pip`:
     ```sh
     pip install jupyter
     ```

2. **Launch Jupyter Notebook**:
   - In the terminal or command prompt, type:
     ```sh
     jupyter notebook
     ```
   - This will start the Jupyter Notebook server and open a new tab in your web browser.

3. **Create and Use Notebooks**:
   - In the Jupyter interface, navigate to the directory where you want to save your notebooks.
   - Click "New" and select "Python 3" to create a new notebook.
   - You can now write and execute Python code in cells. Use `Shift+Enter` to run a cell.


These environments cater to different needs, so you can choose one or more based on your workflow and project requirements.



## Python Syntax and Basics
-----------------------------------

### Writing and Executing Python Programs
---------------------------------------


Writing and executing Python programs can be done in various environments depending on your setup and needs. Here's a guide to doing so in IDLE, VS Code, and Jupyter Notebook:

#### **Using IDLE**

1. **Writing a Python Program in IDLE**:

   - Open IDLE from your applications menu or by running `idle` in your terminal/command prompt.
   - To write a new program, go to `File` -> `New File`. This opens a new editor window.
   - Write your Python code in the editor window. For example:

```python
print("Hello, World!")

```

2. **Saving the Program**:

   - Save your file with a `.py` extension, for example, `hello.py`, by selecting `File` -> `Save`.

3. **Executing the Program**:

   - Run your program by pressing `F5` or by selecting `Run` -> `Run Module` from the menu.
   - The output will be displayed in the Python shell window.


#### **Using Visual Studio Code (VS Code)**

1. **Writing a Python Program in VS Code**:

   - Open VS Code.
   - Open the folder where you want to save your Python files by going to `File` -> `Open Folder`.
   - Create a new file with a `.py` extension, for example, `hello.py`.
   - Write your Python code. For example:
   
```python
print("Hello, World!")
```

2. **Saving the Program**:

   - Save the file by selecting `File` -> `Save` or pressing `Ctrl+S`.

3. **Executing the Program**:

   - Ensure you have the Python extension installed (search for "Python" in the Extensions view and install the one by Microsoft).
   - Open the Command Palette with `Ctrl+Shift+P`, type `Python: Select Interpreter`, and choose your Python interpreter.
   - Run your script by pressing `F5` or right-clicking the editor window and selecting `Run Python File in Terminal`.
   - The output will be displayed in the integrated terminal.

#### **Using Jupyter Notebook**

1. **Writing a Python Program in Jupyter Notebook**:

   - Start Jupyter Notebook by running `jupyter notebook` in your terminal/command prompt. This opens a new tab in your web browser.
   - Navigate to the directory where you want to create your notebook.
   - Click `New` and select `Python 3` to create a new notebook.
   - Write your Python code in a cell. For example:

```python
 print("Hello, World!")
```

2. **Executing the Program**:

   - Execute the code in the cell by pressing `Shift+Enter` or by clicking the `Run` button in the toolbar.
   - The output will be displayed directly below the cell.

**Additional Tips**

- **Running Python Scripts from the Command Line**:

  - You can run a Python script directly from the command line or terminal.
  - Navigate to the directory containing your script and execute it with:

```sh
python hello.py
```

- **Interactive Python Sessions**:

  - For quick testing or interactive work, you can start an interactive Python session by simply typing `python` in your terminal/command prompt.
  - This opens the Python interactive shell where you can execute Python statements line by line.

- **Error Handling**:

  - If your program has errors, the environment will display them. In IDLE and VS Code, you'll see the error message in the shell or terminal.
  - In Jupyter Notebook, the error will appear in the output area below the cell.

By using these environments, you can write, save, and execute Python programs efficiently, leveraging the features that each environment offers for different types of projects and workflows.



### Python IDEs and Code Editors
--------------------------------


1. **PyCharm**

- **PyCharm** is a full-featured IDE developed by JetBrains, designed specifically for Python.

- **Features**:

  - Intelligent code completion
  - Code inspections and quick-fixes
  - Integrated testing
  - Built-in terminal and Python console
  - Git integration
  - Supports web development frameworks like Django and Flask

2. **Visual Studio Code (VS Code)**

- **VS Code** is a lightweight, open-source code editor developed by Microsoft, popular for its versatility and extensive extension support.

- **Features**:

  - Syntax highlighting and IntelliSense
  - Debugging support
  - Integrated terminal
  - Git integration
  - Extensive extensions marketplace (e.g., Python extension by Microsoft)

3. **Jupyter Notebook**

- **Jupyter Notebook** is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations, and narrative text.

- **Features**:

  - Interactive code execution
  - Rich media integration (plots, images, videos)
  - Supports over 40 programming languages
  - Inline data visualization

4. **Spyder**

- **Spyder** is an open-source IDE geared towards data science, offering a MATLAB-like interface.

- **Features**:
  - Integrated IPython console
  - Variable explorer
  - Data visualization tools
  - Code analysis and debugging tools

5. **Thonny**

- **Thonny** is a beginner-friendly Python IDE that is simple and easy to use.

- **Features**:

  - Simple and intuitive interface
  - Built-in debugger
  - Variable tracking
  - Easy to install and set up

6. **Sublime Text**

- **Sublime Text** is a powerful and lightweight text editor known for its speed and simplicity.

- **Features**:

  - Syntax highlighting and code snippets
  - Multiple selections
  - Command palette
  - Plugin ecosystem via Package Control

7. **Atom**

- **Atom** is an open-source text editor developed by GitHub, known for its hackability.

- **Features**:

  - Cross-platform
  - Built-in package manager
  - Smart autocompletion
  - File system browser

8. **Vim**

- **Vim** is a highly configurable text editor built to enable efficient text editing.

- **Features:**

  - Modal editing (different modes for inserting text, navigating, etc.)
  - Extensive plugin system
  - Powerful search and replace
  - Customizable key bindings
  - Lightweight and fast

Choosing the right Python IDE or code editor depends on your specific needs and preferences. Here are some recommendations based on different use cases:

- **Beginners**: Thonny, IDLE
- **General development**: VS Code, PyCharm
- **Data science and research**: Jupyter Notebook, Spyder
- **Lightweight and fast**: Sublime Text, Atom,Vim

Each of these tools offers unique features tailored to different types of projects and workflows.


###	Comments
-----------------------------

- Comments can be used to explain Python code.

- Comments can be used to make the code more readable.

- They are ignored by the Python interpreter and have no effect on the program's execution. 

- There are two types of comments in Python:

  - single-line comments and 
  - multi-line comments.

**single-line comments**

Single-line comments begin with the hash character (`#`) and extend to the end of the line.

```python
print("Hello, World!") #This is a comment
```

**Multi-line Comments**

Python does not have a distinct syntax for multi-line comments like some other programming languages. However, you can use consecutive single-line comments or triple-quoted strings to achieve the same effect.

***Consecutive Single-line Comments***

```python
# This is a multi-line comment
# It spans multiple lines
# Each line starts with a hash character
print("Hello, World!")
```

***Triple-quoted Strings***

Triple-quoted strings (`'''` or `"""`) are primarily used for multi-line strings, but they can also serve as multi-line comments when they are not assigned to a variable or used as a docstring.

```python
"""
This is a multi-line comment
using triple-quoted strings.
It can span multiple lines.
"""
print("Hello, World!")
```


###	Variables and Data Types
---------------------------------------

**Variables:**

- Variables are containers for storing data values.

**Creating Variables:**

- Python has no command for declaring a variable.

- A variable is created the moment you first assign a value to it.

- Example:

```python
x = 5
y = "John"
print(x)
print(y)
```

**Casting:**

- If you want to specify the data type of a variable, this can be done with casting.

- Example:

```python
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
```


**Get the Type:**

- You can get the data type of a variable with the type() function.

- Example:

```python
x = 5
y = "John"
print(type(x))
print(type(y))

```

**Single or Double Quotes?**

- String variables can be declared either by using single or double quotes:

- Example:

```python
x = "John"
# is the same as
x = 'John'

```

**Case-Sensitive**

- Variable names are case-sensitive.

- Example:

This will create two variables:

```python
a = 4
A = "Sally"
#A will not overwrite a
```

**Variable Names**

--------------------

- A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). 

***Rules for Python variables:***

- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)
- A variable name cannot be any of the Python keywords.

- Example:

```python
#Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
```

- Example:

```python
#Illegal variable names:

2myvar = "John"
my-var = "John"
my var = "John"

#Remember that variable names are case-sensitive
```


**Multi Words Variable Names:**

- Variable names with more than one word can be difficult to read.

- There are several techniques you can use to make them more readable:

  - **Camel Case**

    - Each word, except the first, starts with a capital letter:

    ```python
    myVariableName = "John"
    ```
  - **Pascal Case**

    - Each word starts with a capital letter:

    ```python
    MyVariableName = "John"
    ```
  - **Snake Case**

    - Each word is separated by an underscore character:

    ```python
    my_variable_name = "John"
    ```

**One Value to Multiple Variables**

- you can assign the same value to multiple variables in one line:

- Example:

```python
x = y = z = "Orange"
print(x)
print(y)
print(z)
```

**Unpack a Collection**

- If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

Example:

```python
#Unpack a list:

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
```

**Output Variables**

The Python `print()` function is often used to output variables.

- Example:

```python
x = "Python is awesome"
print(x)
```

In the print() function, you output multiple variables, separated by a comma:

- Example:

```python
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
```

> Notice the space character after `"Python "` and `"is "`, without them the result would be "Pythonisawesome".

- For numbers, the `+` character works as a mathematical operator:

- Example:

```python
x = 5
y = 10
print(x + y)
```

- In the print() function, when you try to combine a string and a number with the ``+ operator, Python will give you an error:

- Example:

```python
x = 5
y = "John"
print(x + y) #error
```

- The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:

-  Example:

```python
x = 5
y = "John"
print(x, y)
```

**Variables and Data Structures**

- Variables can also hold complex data types such as lists, dictionaries, tuples, and sets.

```python
# List
my_list = [1, 2, 3]

# Dictionary
my_dict = {"name": "Alice", "age": 25}

# Tuple
my_tuple = (1, 2, 3)

# Set
my_set = {1, 2, 3}

```


**Global Variables**

- Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

- Global variables can be used by everyone, both inside of functions and outside.

- Example:

```python
#Create a variable outside of a function, and use it inside the function

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
```

- If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

Example:

```python
#Create a variable inside a function, with the same name as the global variable

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
```


**The global Keyword**

- Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

- To create a global variable inside a function, you can use the global keyword.

- Example:

  - If you use the global keyword, the variable belongs to the global scope:

```python
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
```

Also, use the global keyword if you want to change a global variable inside a function.

- Example:

  - To change the value of a global variable inside a function, refer to the variable by using the global keyword:

```python

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

```

### Built-in Data Types
-------------------------

- In programming, data type is an important concept.

- Variables can store data of different types, and different types can do different things.

- Python has the following data types built-in by default, in these categories:

```python
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
```


**Numeric Types**

1. **int**: Integer, a whole number, positive or negative, without decimals.

   ```python
   age = 30
   temperature = -5
   ```

2. **float**: Floating-point number, a number with a decimal point.

   ```python
   pi = 3.14
   height = 1.75
   ```

3. **complex**: Complex number, a number with a real and an imaginary part.

   ```python
   complex_num = 2 + 3j
   ```

**Sequence Types**

1. **str**: String, a sequence of characters enclosed in quotes (single, double, or triple).

   ```python
   name = "Alice"
   message = 'Hello, World!'
   multiline = """This is a
   multi-line string."""
   ```

2. **list**: List, an ordered collection of items (which can be of different types), enclosed in square brackets.

   ```python
   fruits = ["apple", "banana", "cherry"]
   numbers = [1, 2, 3, 4.5, "six"]
   ```

3. **tuple**: Tuple, an ordered collection of items similar to a list but immutable, enclosed in parentheses.

   ```python
   coordinates = (10.0, 20.0)
   names = ("Alice", "Bob", "Charlie")
   ```

4. **range**: Range, a sequence of numbers, often used in for-loops.

   ```python
   range_values = range(5)  # 0, 1, 2, 3, 4
   ```

**Mapping Type**

1. **dict**: Dictionary, an unordered collection of key-value pairs, enclosed in curly braces.

   ```python
   person = {"name": "Alice", "age": 30}
   scores = {"math": 95, "science": 90}
   ```

**Set Types**

1. **set**: Set, an unordered collection of unique items, enclosed in curly braces.

   ```python
   unique_numbers = {1, 2, 3, 4, 5}
   ```

2. **frozenset**: Frozen set, an immutable version of a set.

   ```python
   frozen_numbers = frozenset([1, 2, 3, 4, 5])
   ```

**Boolean Type**

1. **bool**: Boolean, represents one of two values: `True` or `False`.

   ```python
   is_active = True
   is_deleted = False
   ```

**Binary Types**

1. **bytes**: Immutable sequence of bytes.

   ```python
   byte_data = b"Hello"
   ```

2. **bytearray**: Mutable sequence of bytes.

   ```python
   byte_array_data = bytearray(5)
   ```

3. **memoryview**: Memory view object allows access to the internal data of an object that supports the buffer protocol without copying.

   ```python
   memory_view = memoryview(byte_data)
   ```

**None Type**

1. **NoneType**: Represents the absence of a value or a null value.
   ```python
   result = None
   ```

###	Control Structures
---------------------------------

#### Conditional Statements (if, elif, else)
--------------------------------------------

Conditional statements in Python are used to execute different blocks of code based on certain conditions. The primary conditional statements are `if`, `elif`, and `else`. 

**`if` Statement**

The `if` statement evaluates a condition, and if it is `True`, it executes the associated block of code.

- Syntax:

```python
if condition:
    # block of code to execute if condition is True

```

```python
# Example: Checking if a number is positive
number = 10
if number > 0:
    print("The number is positive.")  # Output: The number is positive.
```

**`elif` Statement**

The `elif` (short for "else if") statement allows you to check multiple conditions, executing the associated block of code for the first condition that is `True`.

Syntax:

```python

if condition1:
    # block of code to execute if condition1 is True
elif condition2:
    # block of code to execute if condition1 is False and condition2 is True
```

```python
# Example: Checking if a number is positive, negative, or zero
number = 0
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")  # Output: The number is zero.
```

**`else` Statement**

The `else` statement executes a block of code if none of the preceding `if` or `elif` conditions are `True`.

- Syntax:

```python
if condition:
    # block of code to execute if condition is True
else:
    # block of code to execute if condition is False

```

```python
# Example: Checking if a number is positive, negative, or zero
number = -5
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")  # Output: The number is negative.
else:
    print("The number is zero.")
```

**Combining `if`, `elif`, and `else`**

You can combine `if`, `elif`, and `else` statements to create more complex conditional logic.

- Syntax:

```python
if condition1:
    # block of code to execute if condition1 is True
elif condition2:
    # block of code to execute if condition1 is False and condition2 is True
elif condition3:
    # block of code to execute if condition1 and condition2 are False and condition3 is True
else:
    # block of code to execute if none of the above conditions are True

```

```python
# Example: Grading system
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")  # Output: Grade: B
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

**Nested Conditional Statements**

Conditional statements can be nested within each other to handle more complex scenarios.

- Syntax:

```python
if condition1:
    # block of code to execute if condition1 is True
    if nested_condition:
        # block of code to execute if nested_condition is True
    else:
        # block of code to execute if nested_condition is False
elif condition2:
    # block of code to execute if condition1 is False and condition2 is True
    if another_nested_condition:
        # block of code to execute if another_nested_condition is True
    else:
        # block of code to execute if another_nested_condition is False
else:
    # block of code to execute if condition1 and condition2 are False

```

```python
# Example: Checking if a number is positive, negative, or zero and if it is even or odd
number = 8

if number > 0:
    print("The number is positive.")
    if number % 2 == 0:
        print("The number is even.")  # Output: The number is positive. The number is even.
    else:
        print("The number is odd.")
elif number < 0:
    print("The number is negative.")
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("The number is zero.")
```


###	Looping (for, while)
------------------------

Looping in Python allows you to execute a block of code repeatedly. Python supports two main types of loops: `for` loops and `while` loops.

**`for` Loop**

The `for` loop is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string) or other iterable objects.

- Syntax:

```python
for variable in sequence:
    # block of code to execute for each item in the sequence
```

- Example:

```python
# Example: Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry
```

- Example with `range`:

```python
# Example: Using range to iterate over a sequence of numbers
for i in range(5):
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4
```

**`while` Loop**

The `while` loop is used to execute a block of code as long as a specified condition is `True`.

- Syntax:
```python
while condition:
    # block of code to execute while the condition is True
```

- Example:

```python
# Example: Using a while loop to print numbers from 1 to 5
count = 1
while count <= 5:
    print(count)
    count += 1
# Output:
# 1
# 2
# 3
# 4
# 5
```

- **Loop Control Statements**

1. **`break`**: Exits the loop prematurely, regardless of the loop's condition.
2. **`continue`**: Skips the rest of the code inside the loop for the current iteration and moves to the next iteration.
3. **`pass`**: Does nothing; it can be used as a placeholder for future code.

  - Example with `break`:

```python
# Example: Using break to exit a loop
for i in range(10):
    if i == 5:
        break
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4
```

  - Example with `continue`:

```python
# Example: Using continue to skip an iteration
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
# Output:
# 1
# 3
# 5
# 7
# 9
```

  - Example with `pass`:

```python
# Example: Using pass as a placeholder
for i in range(5):
    if i == 3:
        pass  # Placeholder for future code
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4
```

- **Nested Loops**

Loops can be nested within other loops to perform more complex iterations.

- Example:

```python
# Example: Nested for loop to print a multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()
# Output:
# 1 2 3 
# 2 4 6 
# 3 6 9 
```

- **Summary**

- **`for` Loop**: Iterates over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects.
- **`while` Loop**: Repeatedly executes a block of code as long as a condition is `True`.
- **Loop Control Statements**:
  - **`break`**: Exits the loop.
  - **`continue`**: Skips the rest of the code in the current iteration.
  - **`pass`**: Does nothing (placeholder).
- **Nested Loops**: Loops inside other loops to perform complex iterations.

Using loops effectively allows for efficient and readable code for repetitive tasks in Python.


## Data Structures
-------------------------------

### Lists
--------------------

- Lists are used to store multiple items in a single variable.

- Lists are one of 4 built-in data types in Python used to store collections of data.


**Creating Lists**

- Creates a new list with the specified items.

  - **Syntax:**

```python
list_name = [item1, item2, item3, ...]
```
- **list_name**: The variable name for the list.
- **item1, item2, item3, ...**: Elements of the list, separated by commas.

  - **Example:**

```python

# Empty list
empty_list = []

# List of integers 
numbers = [1, 2, 3, 4, 5]

# List of strings
fruits = ["apple", "banana", "cherry"]

# List of mixed data types
mixed_list = [1, "apple", 3.14, True]

```


**The list() Constructor**

- It is also possible to use the list() constructor when creating a new list.

  - **Example:**

```python

#Using the list() constructor to make a List:

fruits = list(("apple", "banana", "cherry")) # note the double round-brackets
print(fruits)
```

**List Items**

- List items are ordered, changeable, and allow duplicate values.

  - Ordered:When we say that lists are ordered, it means that the items have a defined order, and that order will not change.If you add new items to a list, the new items will be placed at the end of the list.(Note: There are some list methods that will change the order, but in general: the order of the items will not change.)

  - Changeable:The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

  - Allow Duplicates:Since lists are indexed, lists can have items with the same value.

     -Example:

```python
     #Lists allow duplicate values:

fruits = ["apple", "banana", "cherry", "apple", "cherry"]
print(fruits)
```

- List items are indexed, the first item has index [0], the second item has index [1] etc.


**Accessing List Items**

- Accesses the item at the specified index in the list.

  - **Syntax:**

```python
list_name[index]
```
- **list_name**: The name of the list.
- **index**: The position of the item to access (starts at 0).

  - **Example:**

```python
fruits = ["apple", "banana", "cherry"]
# Accessing items by positive index
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana

```

  - **Negative Indexing:**

- Negative indexing means start from the end

- `-1` refers to the last item, `-2` refers to the second last item etc.

```python
fruits = ["apple", "banana", "cherry"]
# Accessing items by negative index
print(fruits[-1])  # Output: cherry
print(fruits[-2])  # Output: banana
```

  - **Range of Indexes**

- You can specify a range of indexes by specifying where to start and where to end the range.

- When specifying a range, the return value will be a new list with the specified items.

   - **Example1:**

```python
#Return the third, fourth, and fifth item:

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
```
- Note: The search will start at index 2 (included) and end at index 5 (not included).

- Remember that the first item has index 0.

   - **Example2:**

```python
#This example returns the items from the beginning to, but NOT including, "kiwi":

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[:4])
```

   - **Example3:**

```python
   
#This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[-4:-1])
```

**Modifying List Items**

- Modifies the item at the specified index in the list.

- Lists are mutable, meaning you can change their items.

  - **Syntax:**

```python
list_name[index] = new_value
```
- **list_name**: The name of the list.
- **index**: The position of the item to modify.
- **new_value**: The new value to assign to the list item.

  - **Example:**

```python
fruits[0] = "avocado"  # Changes 'apple' to 'avocado'
print(fruits)  # Output: ['avocado', 'banana', 'cherry']

# Adding an item to the end of the list
fruits.append("date")
print(fruits)  # Output: ['avocado', 'banana', 'cherry', 'date']

# Inserting an item at a specific index
fruits.insert(1, "blueberry")
print(fruits)  # Output: ['avocado', 'blueberry', 'banana', 'cherry', 'date']

```


  - **Change Item Value**

- To change the value of a specific item, refer to the index number:

  - **Example:**

```python
#Change the second item:

fruits = ["apple", "banana", "cherry"]
fruits[1] = "blackcurrant"
print(fruits)
```
  - **Change a Range of Item Values**

- To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

  - **Example:**

```python
#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
fruits[1:3] = ["blackcurrant", "watermelon"]
print(fruits)
```

**Adding Items to a List**

- append()
- insert()

  - **Append Items:**

- To add an item to the end of the list, use the append() method:


    - **Syntax:**

```python
list_name.append(value)
```
- **list_name**: The name of the list.
- **value**: The item to add to the end of the list.

 - **Example1:**

```python

# Adding an item to the end of the list

fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print(fruits) 

```
- **Example2:**
```python
fruits = ["apple", "banana", "cherry"]
fruits.append(2)
print(fruits) 

```
  - **Extend List**

- To append elements from another list to the current list, use the extend() method.

 - **Example1:**

```python
#Add the elements of tropical to fruits:

fruits = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
fruits.extend(tropical)
print(fruits)

```

  - The `extend()` method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

 - **Example1:**

```python
#Add elements of a tuple to a list:

list1 = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
list1.extend(thistuple)
print(list1)
```


  - **Insert Items**

- To insert a list item at a specified index, use the insert() method.

- The insert() method inserts an item at the specified index.


    - **Syntax:**

```python
list_name.insert(index, value)
```
- **list_name**: The name of the list.
- **index**: The position at which to insert the new item.
- **value**: The item to insert.

    - **Example:**

```python
# Inserting an item at a specific index

fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "blueberry")   # Inserts 'blueberry' at index 1
print(fruits) 

```

**Removing Items from a List**

  - ***Remove Specified Item:***

- The remove() method removes the specified item.
- Removes the first occurrence of the specified value from the list.

  - **Syntax:**

```python
list_name.remove(value)
```
- **list_name**: The name of the list.
- **value**: The item to remove from the list.

  -  **Example:**
```python

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")  # Removes 'banana' from the list
print(fruits)
```

  - ***Remove Specified Index***

- The `pop()` method removes the specified index.
- Removes the item at the specified index and returns it.

  - **Syntax:**

```python
list_name.pop(index)
```
- **list_name**: The name of the list.
- **index**: The position of the item to remove (optional, removes last item if not specified).

  - **Example:**

```python

fruits = ["apple", "banana", "cherry"]
removed_item = fruits.pop(2)  # Removes and returns the item at index 2
print(fruits)

```

  - If you do not specify the index, the pop() method removes the last item.

  - **Syntax:**

```python
list_name.pop()
```
- **list_name**: The name of the list.

  - **Example:**

```python
fruits = ["apple", "banana", "cherry"]
last_item = fruits.pop()  # Removes and returns the last item in the list
print(fruits)
```

  - The `del` keyword also removes the specified index.

  - **Example:**

```python
#Remove the first item:

fruits = ["apple", "banana", "cherry"]
del fruits[0]
print(fruits)
```


  - The `del` keyword can also delete the list completely.

  - **Example:**

```python
#Delete the entire list:

fruits= ["apple", "banana", "cherry"]
del fruits
print(fruits)
```
 
  - **Clear the List**

- Removes all items from the list.

  - **Syntax:**
```python
list_name.clear()
```
- **list_name**: The name of the list.

  - **Example:**

```python

fruits= ["apple", "banana", "cherry"]
fruits.clear()  # Removes all items from the list
print(fruits)

```



**List Methods**
--------------------

- Python has a set of built-in methods that you can use on lists.

| Method     | Description                                                |
|------------|------------------------------------------------------------|
| append() | Adds an element at the end of the list                     |
| clear()  | Removes all the elements from the list                     |
| copy()   | Returns a copy of the list                                 |
| count()  | Returns the number of elements with the specified value    |
| extend() | Adds the elements of a list (or any iterable) to the end of the current list |
| index()  | Returns the index of the first element with the specified value |
| insert() | Adds an element at the specified position                  |
| pop()    | Removes the element at the specified position              |
| remove() | Removes the item with the specified value                  |
| reverse()| Reverses the order of the list                             |
| sort()   | Sorts the list                                             |

-  **Finding the Index of an Item**

  - Returns the index of the first occurrence of the specified value.

  - **Syntax:**

```python
list_name.index(value)
```
- **list_name**: The name of the list.
- **value**: The item to find in the list.

  - **Example:**

```python

fruits= ["apple", "banana", "cherry"]
index = fruits.index("banana")  # Finds the index of 'banana'
print(index)
```


- **Counting Occurrences of an Item**

  - Returns the number of times the specified value appears in the list.

  - **Syntax:**

```python
list_name.count(value)
```
- **list_name**: The name of the list.
- **value**: The item to count in the list.

  - **Example:**

```python

fruits = ["apple", "banana", "cherry"]
count = fruits.count("cherry")  # Counts occurrences of 'cherry'
print(count)

```

- **Sorting the List**

  - Sorts the items of the list in ascending order.

  - **Syntax:**

```python
list_name.sort()
```
- **list_name**: The name of the list.

  - **Example:**

```python

fruits = ["apple", "banana","grapes", "cherry"]
fruits.sort()  # Sorts the list in ascending order
print(fruits)

```
  - **Sort Descending**

    - To sort `descending`, use the keyword argument reverse = True.

  - **Example1:**

```python
#Sort the list descending:

fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruits.sort(reverse = True)
print(fruits)

```

  - **Example2:**

```python
#Sort the list descending:

num = [100, 50, 65, 82, 23]
num.sort(reverse = True)
print(num)
```

- **Reversing the List**

  - Reverses the order of the items in the list.

  - **Syntax:**

```python
list_name.reverse()
```
- **list_name**: The name of the list.

  - **Example:**

```python

fruits = ["apple", "banana", "cherry"]
fruits.reverse()  # Reverses the order of the list
print(fruits)

```

- **Copying the List**


- Returns a shallow copy of the list.

  - **Syntax:**

```python
list_name.copy()
```
- **list_name**: The name of the list.

  - **Example:**

```python

fruits = ["apple", "banana", "cherry"]
fruits_copy = fruits.copy()  # Creates a copy of the list
print(fruits_copy) 

```

**List Comprehensions**
-------------------------

- Creates a new list by applying an expression to each item in an iterable, optionally filtering items with a condition.

  - **Syntax:**

```python
new_list = [expression for item in iterable if condition]
```

- **new_list**: The new list being created.
- **expression**: The expression to evaluate for each item.
- **item**: The variable representing each element in the iterable.
- **iterable**: The collection being iterated over.
- **condition**: (Optional) A condition to filter items.

  - **Example:**

```python

# Creating a list of squares using a for loop
squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Creating a list of squares using list comprehension
squares = [x ** 2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Filtering items using list comprehension
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)  # Output: [0, 4, 16, 36, 64]

```

**Slicing Lists**
---------------------


- Extracts a portion of the list from the start index to the stop index, optionally using a step.

  - **Syntax:**

```python
list_name[start:stop:step]
```

- **list_name**: The name of the list.
- **start**: The starting index (inclusive).
- **stop**: The ending index (exclusive).
- **step**: (Optional) The step size (default is 1).

  - **Example:**

```python

# Creating a list 
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slicing from index 2 to 5
slice1 = numbers[2:6]
print(slice1)  # Output: [2, 3, 4, 5]

# Slicing from the beginning to index 4
slice2 = numbers[:5]
print(slice2)  # Output: [0, 1, 2, 3, 4]

# Slicing from index 5 to the end
slice3 = numbers[5:]
print(slice3)  # Output: [5, 6, 7, 8, 9]

# Slicing the entire list with a step of 2
slice4 = numbers[::2]
print(slice4)  # Output: [0, 2, 4, 6, 8]

# Reversing the list using slicing
reversed_numbers = numbers[::-1]
print(reversed_numbers)  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

```


**Join Lists**

- There are several ways to join, or concatenate, two or more lists in Python.

- One of the easiest ways are by using the + operator.

  - **Example:**

```python
#Join two list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
```


### Tuples
------------------

- Tuples are used to store multiple items in a single variable.
- A tuple is an immutable, ordered collection of items in Python. Once created, the items of a tuple cannot be changed, added, or removed. Tuples are used to group related data together.

**Creating Tuples**

  - **Syntax:**

```python
tuple_name = (item1, item2, item3, ...)

```

- **tuple_name**: The variable name for the tuple.
- **item1, item2, item3, ...**: Elements of the tuple, separated by commas.

  - **Examples:**

```python

# Empty tuple
empty_tuple = ()

# Tuple of integers
numbers = (1, 2, 3, 4, 5)

# Tuple of strings
fruits = ("apple", "banana", "cherry")

# Tuple of mixed data types
mixed_tuple = (1, "apple", 3.14, True)

```

**Accessing Tuple Items**

- Accesses the item at the specified index in the tuple.

  - **Syntax:**
  

```python
tuple_name[index]

```

- **tuple_name**: The name of the tuple.
- **index**: The position of the item to access (starts at 0).

  - **Examples:**

```python

fruits = ("apple", "banana", "cherry")
# Accessing items by positive index
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana

# Accessing items by negative index
print(fruits[-1])  # Output: cherry
print(fruits[-2])  # Output: banana

```

**Unpacking Tuples**

- Assigns the items of a tuple to multiple variables.

  - **Syntax:**

```python
var1, var2, var3, ... = tuple_name

```
- **var1, var2, var3, ...**: Variables to assign the tuple's items to.
- **tuple_name**: The name of the tuple.

#### Examples:

```python

# Unpacking a tuple into variables
numbers = (1, 2, 3)
a, b, c = numbers
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

# Using an asterisk to capture remaining items
fruits = ("apple", "banana", "cherry", "date")
first_fruit, *remaining_fruits = fruits
print(first_fruit)  # Output: apple
print(remaining_fruits)  # Output: ['banana', 'cherry', 'date']

```

**Tuple Methods**

- **Counting Occurrences of an Item**


  - Returns the number of times the specified value appears in the tuple.

- **Syntax:**

```python
tuple_name.count(value)
```
- **tuple_name**: The name of the tuple.
- **value**: The item to count in the tuple.

  - **Example:**

```python

fruits = ("apple", "banana", "cherry", "date")
count = fruits.count("cherry")  # Counts occurrences of 'cherry'
print(count)  # Output: 1

```

- **Finding the Index of an Item**

  - Returns the index of the first occurrence of the specified value.

  - **Syntax:**

```python
tuple_name.index(value)

```

- **tuple_name**: The name of the tuple.
- **value**: The item to find in the tuple.

  - **Example:**

```python
fruits = ("apple", "banana", "cherry", "date")
index = fruits.index("banana")  # Finds the index of 'banana'
print(index)  # Output: 1

```

**Nested Tuples**
-------------------

- Tuples can contain other tuples as items, creating a nested structure.

  - **Syntax:**

```python
tuple_name = (tuple1, tuple2, ...)

```
- **tuple_name**: The variable name for the tuple.
- **tuple1, tuple2, ...**: Nested tuples as elements of the main tuple.

  - **Example:**

```python
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple[0])  # Output: (1, 2)
print(nested_tuple[0][1])  # Output: 2

```

**Slicing Tuples**
-------------------------

- Extracts a portion of the tuple from the start index to the stop index, optionally using a step.

  - **Syntax:**

```python
tuple_name[start:stop:step]

```

- **tuple_name**: The name of the tuple.
- **start**: The starting index (inclusive).
- **stop**: The ending index (exclusive).
- **step**: (Optional) The step size (default is 1).

  - **Example:**

```python
# Creating a tuple for demonstration
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Slicing from index 2 to 5
slice1 = numbers[2:6]
print(slice1)  # Output: (2, 3, 4, 5)

# Slicing from the beginning to index 4
slice2 = numbers[:5]
print(slice2)  # Output: (0, 1, 2, 3, 4)

# Slicing from index 5 to the end
slice3 = numbers[5:]
print(slice3)  # Output: (5, 6, 7, 8, 9)

# Slicing the entire tuple with a step of 2
slice4 = numbers[::2]
print(slice4)  # Output: (0, 2, 4, 6, 8)

# Reversing the tuple using slicing
reversed_numbers = numbers[::-1]
print(reversed_numbers)  # Output: (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

```


### Sets 
---------------------


- A set is an `unordered` collection of unique elements(no duplicate values) in Python. 
- Sets are `mutable`, meaning you can add or remove items after creating them. However, each element must be immutable (e.g., numbers, strings, tuples).

**Creating Sets**

  - **Syntax:**

```python
set_name = {item1, item2, item3, ...}

```

- **set_name**: The variable name for the set.
- **item1, item2, item3, ...**: Elements of the set, separated by commas.

  - **Examples:**

```python
# Empty set
empty_set = set()

# Set of integers
numbers = {1, 2, 3, 4, 5}

# Set of strings
fruits = {"apple", "banana", "cherry"}

# Set with mixed data types
mixed_set = {1, "apple", 3.14, True}
```

**Adding Items to a Set**


- Adds a new item to the set.

  - **Syntax:**

```python
set_name.add(value)
```

- **set_name**: The name of the set.
- **value**: The item to add to the set.

  - **Example:**

```python

fruits = {"apple", "banana", "cherry"}
fruits.add("date")
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'date'}

```

- To add items from another set into the current set, use the update() method.

  - **Example**

```python
#Add elements from tropical into fruits:

fruits = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

fruits.update(tropical)

print(fruits)

```

**Removing Items from a Set**

- Removes a specific item from the set. If the item does not exist, it raises a `KeyError`.
**
  - **Syntax:**

```python
set_name.remove(value)
```

- **set_name**: The name of the set.
- **value**: The item to remove from the set.

  - **Example:**

```python

fruits = {"apple", "banana", "cherry","date"}
fruits.remove("banana")
print(fruits)  # Output: {'apple', 'cherry', 'date'}
```

- Removes a specific item from the set. If the item does not exist, it does nothing.

  - **Syntax:**

```python
set_name.discard(value)
```

- **set_name**: The name of the set.
- **value**: The item to remove from the set.

  - **Example:**

```python

fruits = {"apple", "banana", "cherry","date"}
fruits.discard("banana")  # 'banana' is already removed, so nothing happens
print(fruits)  # Output: {'apple', 'cherry', 'date'}

```


- Removes and returns an arbitrary item from the set.

  - **Syntax:**

```python
set_name.pop()
```
- **set_name**: The name of the set.

  - **Example:**

```python

fruits = {"apple", "banana", "cherry","date"}
item = fruits.pop()
print(item)  # Output: 'apple' (example, actual item may vary)
print(fruits)  # Output: {'cherry', 'date'} (example, actual items may vary)

```

- Removes all items from the set.

  - **Syntax:**

```python
set_name.clear()
```

- **set_name**: The name of the set.

  - **Example:**

```python

fruits = {"apple", "banana", "cherry","date"}
fruits.clear()
print(fruits)  # Output: set()

```

**Set Operations**
------------------------

  - **Union of Sets**

    - Returns a set containing all unique items from both sets.

    - **Syntax:**

```python
set1.union(set2)
# or
set1 | set2
```

- **set1, set2**: The sets to perform the union operation on.

    - **Example:**

```python
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a.union(set_b)
# or
union_set = set_a | set_b
print(union_set)  # Output: {1, 2, 3, 4, 5}

```

  - **Intersection of Sets**


- Returns a set containing only the items that are present in both sets.

    - **Syntax:**

```python
set1.intersection(set2)
# or
set1 & set2
```

- **set1, set2**: The sets to perform the intersection operation on.

    - **Example:**

```python

set_a = {1, 2, 3}
set_b = {3, 4, 5}
intersection_set = set_a.intersection(set_b)
# or
intersection_set = set_a & set_b
print(intersection_set)  # Output: {3}

```

  - **Difference of Sets**

- Returns a set containing items that are in the first set but not in the second set.

    - **Syntax:**

```python
set1.difference(set2)
# or
set1 - set2

```

- **set1, set2**: The sets to perform the difference operation on.

    - **Example:**

```python

set_a = {1, 2, 3}
set_b = {3, 4, 5}

difference_set = set_a.difference(set_b)
# or
difference_set = set_a - set_b
print(difference_set)  # Output: {1, 2}

```

  - **Symmetric Difference of Sets**


    - Returns a set containing items that are in either set, but not in both.

    - **Syntax:**

```python
set1.symmetric_difference(set2)
# or
set1 ^ set2

```
- **set1, set2**: The sets to perform the symmetric difference operation on.

    - **Example:**

```python

set_a = {1, 2, 3}
set_b = {3, 4, 5}

symmetric_difference_set = set_a.symmetric_difference(set_b)
# or
symmetric_difference_set = set_a ^ set_b
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}

```

**Checking Membership**

- Checks if an item is in the set.

  - **Syntax:**

```python
item in set_name
```

- **item**: The item to check for membership.
- **set_name**: The name of the set.

  - **Example:**

```python

fruits = {"apple", "banana", "cherry","date"}
print("apple" in fruits)  # Output: False
print("date" in fruits)   # Output: True

```


### Dictionaries
---------------------

-  A dictionary is an unordered collection of key-value pairs in Python.
-  Dictionaries are mutable, meaning you can add, remove, or change items after creating them. Keys must be immutable (e.g., numbers, strings, tuples), but values can be of any type.

**Creating Dictionaries**

- **Syntax:**

```python
dict_name = {key1: value1, key2: value2, ...}
```

- **dict_name**: The variable name for the dictionary.
- **key1, key2, ...**: The keys in the dictionary.
- **value1, value2, ...**: The values associated with the keys.

- **Examples:**

```python
# Empty dictionary
empty_dict = {}

# Dictionary with integer keys and string values
numbers_dict = {1: "one", 2: "two", 3: "three"}

# Dictionary with string keys and mixed values
person = {"name": "John", "age": 30, "city": "New York"}

# Dictionary with mixed data types
mixed_dict = {1: "apple", "color": "red", 3.14: [1, 2, 3]}
```

**Accessing Values in a Dictionary**

- Access values using their keys.

- **Syntax:**

```python
dict_name[key]
```

- **dict_name**: The name of the dictionary.
- **key**: The key whose value you want to access.

- **Example:**

```python
person = {"name": "John", "age": 30, "city": "New York"}
print(person["name"])  # Output: John
print(person["age"])   # Output: 30
```

**Adding or Updating Items in a Dictionary**

- Add a new key-value pair or update an existing key with a new value.

- **Syntax:**

```python
dict_name[key] = value
```

- **dict_name**: The name of the dictionary.
- **key**: The key to add or update.
- **value**: The value to assign to the key.

- **Example:**

```python
person = {"name": "John", "age": 30}
person["city"] = "New York"  # Adding a new key-value pair
person["age"] = 31  # Updating an existing key with a new value
print(person)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}
```

**Removing Items from a Dictionary**

- Removes a specific key-value pair from the dictionary. Raises a `KeyError` if the key does not exist.

- **Syntax:**

```python
del dict_name[key]
```

- **dict_name**: The name of the dictionary.
- **key**: The key to remove.

- **Example:**

```python
person = {"name": "John", "age": 30, "city": "New York"}
del person["age"]
print(person)  # Output: {'name': 'John', 'city': 'New York'}
```

- Removes a specific key-value pair and returns the value. Raises a `KeyError` if the key does not exist.

- **Syntax:**

```python
dict_name.pop(key)
```

- **dict_name**: The name of the dictionary.
- **key**: The key to remove.

- **Example:**

```python
person = {"name": "John", "age": 30, "city": "New York"}
age = person.pop("age")
print(age)     # Output: 30
print(person)  # Output: {'name': 'John', 'city': 'New York'}
```

- Removes all items from the dictionary.

- **Syntax:**

```python
dict_name.clear()
```

- **dict_name**: The name of the dictionary.

- **Example:**

```python
person = {"name": "John", "age": 30, "city": "New York"}
person.clear()
print(person)  # Output: {}
```

**Dictionary Operations**

------------------------

- **Checking Membership**

  - Checks if a key is in the dictionary.

  - **Syntax:**

  ```python
  key in dict_name
  ```

  - **key**: The key to check for membership.
  - **dict_name**: The name of the dictionary.

  - **Example:**

  ```python
  person = {"name": "John", "age": 30, "city": "New York"}
  print("name" in person)  # Output: True
  print("address" in person)  # Output: False
  ```

- **Iterating Through a Dictionary**

  - **Syntax:**

  ```python
  for key in dict_name:
      # Access the key
      # Access the value using dict_name[key]
  ```

  - **dict_name**: The name of the dictionary.

  - **Example:**

  ```python
  person = {"name": "John", "age": 30, "city": "New York"}
  for key in person:
      print(f"{key}: {person[key]}")
  # Output:
  # name: John
  # age: 30
  # city: New York
  ```

**Dictionary Methods**

- **`items()`**: Returns a view object that displays a list of a dictionary's key-value tuple pairs.

  - **Syntax:**

  ```python
  dict_name.items()
  ```

  - **Example:**

  ```python
  person = {"name": "John", "age": 30, "city": "New York"}
  print(person.items())  # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])
  ```

- **`keys()`**: Returns a view object that displays a list of all the keys in the dictionary.

  - **Syntax:**

  ```python
  dict_name.keys()
  ```

  - **Example:**

  ```python
  person = {"name": "John", "age": 30, "city": "New York"}
  print(person.keys())  # Output: dict_keys(['name', 'age', 'city'])
  ```

- **`values()`**: Returns a view object that displays a list of all the values in the dictionary.

  - **Syntax:**

  ```python
  dict_name.values()
  ```

  - **Example:**

  ```python
  person = {"name": "John", "age": 30, "city": "New York"}
  print(person.values())  # Output: dict_values(['John', 30, 'New York'])
  ```

- **`get()`**: Returns the value for a specified key if the key is in the dictionary. If the key is not found, it returns `None` or a specified default value.

  - **Syntax:**

  ```python
  dict_name.get(key, default_value)
  ```

  - **key**: The key to search for.
  - **default_value**: (Optional) The value to return if the key is not found.

  - **Example:**

  ```python
  person = {"name": "John", "age": 30, "city": "New York"}
  print(person.get("name"))  # Output: John
  print(person.get("address", "Unknown"))  # Output: Unknown
  ```

- **`update()`**: Updates the dictionary with the key-value pairs from another dictionary or an iterable of key-value pairs.

  - **Syntax:**

  ```python
  dict_name.update(other_dict)
  ```

  - **other_dict**: Another dictionary or an iterable of key-value pairs.

  - **Example:**

  ```python
  person = {"name": "John", "age": 30}
  updates = {"city": "New York", "age": 31}
  person.update(updates)
  print(person)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}
  ```


### Functions and Modules in Python

#### Defining Functions
---------------------

- Functions are blocks of reusable code that perform a specific task.

- **Syntax:**

```python
def function_name(parameters):
    """
    Docstring (optional): Brief explanation of the function.
    """
    # Function body
    return value
```

- **function_name**: The name of the function.
- **parameters**: Optional; the input values for the function.
- **return**: Optional; the value returned by the function.

- **Example:**

```python
def greet(name):
    """
    Function to greet a person by name.
    """
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
```

#### Function Arguments and Return Values
---------------------

- **Positional Arguments**: Arguments passed to the function in the order they are defined.

- **Example:**

```python
def add(a, b):
    return a + b

print(add(2, 3))  # Output: 5
```

- **Keyword Arguments**: Arguments passed to the function by explicitly naming the parameter.

- **Example:**

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet(name="Alice", greeting="Hi"))  # Output: Hi, Alice!
```

- **Default Arguments**: Arguments that assume a default value if not provided.

- **Example:**

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
```

- **Arbitrary Arguments**: Functions can accept an arbitrary number of positional or keyword arguments using `*args` and `**kwargs`.

- **Example:**

```python
def add(*args):
    return sum(args)

print(add(1, 2, 3, 4))  # Output: 10

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30)  # Output: name: Alice \n age: 30
```

#### Lambda Functions
---------------------
Lambda functions are small anonymous functions defined with the `lambda` keyword.

- **Syntax:**

```python
lambda arguments: expression
```

- **Example:**

```python
add = lambda a, b: a + b
print(add(2, 3))  # Output: 5

# Using lambda with map() function
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]
```

#### Built-in Functions
---------------------

Python provides many built-in functions for various tasks.

- **Examples:**

```python
# len(): Returns the length of an object
print(len("hello"))  # Output: 5

# type(): Returns the type of an object
print(type(5))  # Output: <class 'int'>

# range(): Generates a sequence of numbers
print(list(range(5)))  # Output: [0, 1, 2, 3, 4]

# sum(): Sums the elements of an iterable
print(sum([1, 2, 3]))  # Output: 6

# max(): Returns the largest item in an iterable
print(max([1, 2, 3]))  # Output: 3

# min(): Returns the smallest item in an iterable
print(min([1, 2, 3]))  # Output: 1
```

#### Importing Modules and Packages
---------------------
Modules are files containing Python code (functions, classes, variables) which can be imported and used in other scripts.

- **Syntax:**

```python
import module_name
```

- **Examples:**

```python
import math
print(math.sqrt(16))  # Output: 4.0

import random
print(random.randint(1, 10))  # Output: Random integer between 1 and 10
```

- Importing specific items from a module:

```python
from module_name import item1, item2

# Example:
from math import sqrt, pi
print(sqrt(16))  # Output: 4.0
print(pi)  # Output: 3.141592653589793
```

- Importing a module with an alias:

```python
import module_name as alias

# Example:
import numpy as np
print(np.array([1, 2, 3]))  # Output: [1 2 3]
```

#### Creating and Using Custom Modules
---------------------
You can create your own modules by saving Python code in `.py` files and then importing them.

- **Creating a custom module (my_module.py):**

```python
# my_module.py

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b
```

- **Using the custom module:**

```python
# main.py

import my_module

print(my_module.greet("Alice"))  # Output: Hello, Alice!
print(my_module.add(2, 3))  # Output: 5

# Importing specific items from the custom module
from my_module import greet, add

print(greet("Bob"))  # Output: Hello, Bob!
print(add(4, 5))  # Output: 9
```

- **Creating a package:**

A package is a directory with a special `__init__.py` file that can contain multiple modules.

- **Package structure:**

```
my_package/
    __init__.py
    module1.py
    module2.py
```

- **Using the package:**

```python
# main.py

from my_package import module1, module2

# Assuming module1.py and module2.py have their own functions
print(module1.function1())
print(module2.function2())
```

## File Handling in Python
-----------------------


#### Reading and Writing Files
---------------------

Python provides built-in functions for reading from and writing to files.

##### Opening and Closing Files

- **Syntax:**

```python
file_object = open("filename", "mode")
```

- **filename**: The name of the file to be opened.
- **mode**: The mode in which the file is opened. Common modes are:
  - `'r'`: Read (default)
  - `'w'`: Write (creates a new file or truncates an existing file)
  - `'a'`: Append (writes data to the end of the file)
  - `'b'`: Binary mode
  - `'t'`: Text mode (default)
  - `'+'`: Update mode (read and write)

- **Example:**

```python
# Opening a file in read mode
file = open("example.txt", "r")

# Reading the content
content = file.read()

# Closing the file
file.close()
```

##### Reading Files

- **read()**: Reads the entire file.

  - **Example:**

  ```python
  with open("example.txt", "r") as file:
      content = file.read()
      print(content)
  ```

- **readline()**: Reads a single line from the file.

  - **Example:**

  ```python
  with open("example.txt", "r") as file:
      line = file.readline()
      print(line)
  ```

- **readlines()**: Reads all the lines and returns them as a list.

  - **Example:**

  ```python
  with open("example.txt", "r") as file:
      lines = file.readlines()
      for line in lines:
          print(line)
  ```

##### Writing Files

- **write()**: Writes a string to the file.

  - **Example:**

  ```python
  with open("example.txt", "w") as file:
      file.write("Hello, World!")
  ```

- **writelines()**: Writes a list of strings to the file.

  - **Example:**

  ```python
  lines = ["First line\n", "Second line\n", "Third line\n"]
  with open("example.txt", "w") as file:
      file.writelines(lines)
  ```

**Appending to Files**

- **Example:**

```python
with open("example.txt", "a") as file:
    file.write("\nNew line added.")
```

#### Working with CSV Files
---------------------

The `csv` module in Python provides functionality to read from and write to CSV files.

**Reading CSV Files**

- **Using csv.reader()**: Reads CSV files into a list of lists.

  - **Example:**

  ```python
  import csv

  with open("data.csv", "r") as file:
      reader = csv.reader(file)
      for row in reader:
          print(row)
  ```

- **Using csv.DictReader()**: Reads CSV files into a list of dictionaries.

  - **Example:**

  ```python
  import csv

  with open("data.csv", "r") as file:
      reader = csv.DictReader(file)
      for row in reader:
          print(row)
  ```

**Writing CSV Files**

- **Using csv.writer()**: Writes data to CSV files.

  - **Example:**

  ```python
  import csv

  data = [
      ["Name", "Age", "City"],
      ["Alice", 30, "New York"],
      ["Bob", 25, "Los Angeles"]
  ]

  with open("output.csv", "w", newline="") as file:
      writer = csv.writer(file)
      writer.writerows(data)
  ```

- **Using csv.DictWriter()**: Writes dictionaries to CSV files.

  - **Example:**

  ```python
  import csv

  data = [
      {"Name": "Alice", "Age": 30, "City": "New York"},
      {"Name": "Bob", "Age": 25, "City": "Los Angeles"}
  ]

  with open("output.csv", "w", newline="") as file:
      fieldnames = ["Name", "Age", "City"]
      writer = csv.DictWriter(file, fieldnames=fieldnames)

      writer.writeheader()
      writer.writerows(data)
  ```

Certainly! Here's an expanded version with syntax examples for each file operation in Python:

### File Operations in Python

- **Opening and Closing Files**

- **Opening Files**: Files in Python are opened using the `open()` function, which returns a file object.

  ```python
  file = open("filename.txt", "mode")
  ```

  - **filename**: Name of the file to be opened.
  - **mode**: Specifies the mode in which the file is opened (`'r'` for read, `'w'` for write, `'a'` for append, `'b'` for binary, `'t'` for text).

  **Example:**

  ```python
  file = open("example.txt", "r")
  ```

- **Reading from Files**: Once opened, files can be read using various methods like `read()`, `readline()`, or `readlines()`.

  ```python
  content = file.read()     # Reads entire file content
  line = file.readline()    # Reads one line from the file
  lines = file.readlines()  # Reads all lines into a list
  ```

- **Writing to Files**: Writing to files is done using the `write()` or `writelines()` methods.

  ```python
  file.write("Hello, World!")          # Writes a string to the file
  file.writelines(["line1\n", "line2\n"])  # Writes a list of lines to the file
  ```

- **Appending to Files**: Files can be opened in append mode (`'a'`), and new content is added at the end of the file.

  ```python
  file = open("example.txt", "a")
  file.write("New content")
  ```

- **Closing Files**: It's important to close files after operations are complete to free up system resources.

  ```python
  file.close()
  ```

**Context Managers (with Statement)**

- Python's `with` statement ensures that resources are properly managed. It automatically closes the file when execution leaves the `with` block.

**Example:**

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
# File automatically closed after the block
```

**Checking File Existence and Properties**

- **Checking Existence**: Use `os.path.exists()` to check if a file exists.

  ```python
  import os
  if os.path.exists("example.txt"):
      print("File exists")
  ```

- **Getting File Information**: Use `os.stat()` to get file information like size, permissions, and timestamps.

  ```python
  import os
  file_info = os.stat("example.txt")
  print(f"Size of file: {file_info.st_size} bytes")
  ```

**Deleting Files**

- **Deleting Files**: Use `os.remove()` to delete a file.

  ```python
  import os
  os.remove("example.txt")
  ```

**Handling Exceptions**

- **Error Handling**: Use try-except blocks to handle file operation errors gracefully.

  ```python
  try:
      file = open("example.txt", "r")
      content = file.read()
  except FileNotFoundError:
      print("File not found")
  finally:
      file.close()  # Ensure file is closed
  ```

**Working with Directories**

- **Creating Directories**: Use `os.makedirs()` to create directories.

  ```python
  import os
  os.makedirs("path/to/directory")
  ```

- **Listing Files in a Directory**: Use `os.listdir()` to get a list of files in a directory.

  ```python
  import os
  files = os.listdir("path/to/directory")
  print(files)
  ```

## OOPs
------------------------------

Object-Oriented Programming (OOP) in Python is a paradigm that uses classes and objects to model real-world entities and their interactions. Below is an in-depth look at the main OOP concepts:

### Classes and Objects

**Classes** are blueprints for creating objects. They encapsulate data for the object and methods to manipulate that data.

**Objects** are instances of classes. They represent real-world entities with attributes (data) and behavior (methods).

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object (instance) of the Person class
person1 = Person("Alice", 30)
person1.greet()  # Output: Hello, my name is Alice and I am 30 years old.
```

### Methods

**Methods** are functions defined within a class that describe the behaviors of the objects.

- **Instance Methods**: Operate on an instance of the class. They can access and modify the object’s attributes.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

circle1 = Circle(5)
print(circle1.area())  # Output: 78.5
```

- **Class Methods**: Defined using the `@classmethod` decorator, they operate on the class itself rather than an instance. They can access class attributes.

```python
class Math:
    @classmethod
    def add(cls, a, b):
        return a + b

result = Math.add(5, 3)
print(result)  # Output: 8
```

- **Static Methods**: Defined using the `@staticmethod` decorator, they don’t operate on an instance or the class. They are utility methods that belong to the class’s namespace.

```python
class Utility:
    @staticmethod
    def multiply(a, b):
        return a * b

result = Utility.multiply(4, 5)
print(result)  # Output: 20
```

### Inheritance

**Inheritance** allows a class to inherit attributes and methods from another class, promoting code reuse.

- **Base (Parent) Class**: The class being inherited from.
- **Derived (Child) Class**: The class that inherits from the base class.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):   
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
```

### Polymorphism

**Polymorphism** allows methods to be used interchangeably among objects of different classes that share the same method name.

```python
class Bird:
    def fly(self):
        print("Bird can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguin can't fly but can swim")

def test_fly(bird):
    bird.fly()

bird = Bird()
penguin = Penguin()

test_fly(bird)    # Output: Bird can fly
test_fly(penguin)  # Output: Penguin can't fly but can swim
```

### Encapsulation and Abstraction

**Encapsulation** is the bundling of data (attributes) and methods that operate on the data within one unit (class), restricting access to some of the object's components.

- **Private Attributes/Methods**: Prefixed with double underscores `__`, they cannot be accessed directly from outside the class.

```python
class Encapsulated:
    def __init__(self, value):
        self.__private_value = value

    def get_value(self):
        return self.__private_value

obj = Encapsulated(10)
print(obj.get_value())  # Output: 10
# print(obj.__private_value)  # AttributeError: 'Encapsulated' object has no attribute '__private_value'
```

**Abstraction** hides the complex implementation details and shows only the essential features of the object. This can be achieved through abstract classes and methods in Python using the `abc` module.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(10, 5)
print(rect.area())  # Output: 50
```

## Error and Exception Handling
---------------------------------

Error and exception handling in Python is crucial for writing robust and reliable programs. It helps you manage errors gracefully and ensures that your program can handle unexpected situations without crashing.

### Understanding Errors and Exceptions

Errors in Python are broadly categorized into two types:

1. **Syntax Errors**: These occur when the parser detects an incorrect syntax. They are typically caught by the interpreter when the code is being parsed, and they must be corrected before the program can run.

   ```python
   # Example of a syntax error
   if True
       print("This is a syntax error")
   ```

2. **Exceptions**: These are errors detected during execution. They are raised by the Python interpreter or manually using the `raise` statement.

   Common exceptions include:
   - `ZeroDivisionError`: Division by zero.
   - `IndexError`: Index out of range.
   - `KeyError`: Key not found in a dictionary.
   - `ValueError`: Invalid value.
   - `TypeError`: Invalid type.
   - `FileNotFoundError`: File not found.

### Try, Except, Finally

Python uses `try`, `except`, and `finally` blocks to handle exceptions.

1. **Try Block**: Contains code that might raise an exception.

2. **Except Block**: Contains code that is executed if an exception occurs in the `try` block.

3. **Finally Block**: Contains code that is always executed, regardless of whether an exception occurred or not. It is typically used for cleanup actions (like closing files).

**Basic Example:**

```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handling the specific exception
    print("Cannot divide by zero!")
finally:
    # Code that will run no matter what
    print("Execution finished.")
```

**Handling Multiple Exceptions:**

You can handle multiple exceptions by specifying different `except` blocks for each exception type.

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution finished.")
```

**Using Else with Try-Except:**

The `else` block can be used to execute code if the `try` block does not raise an exception.

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")
else:
    print(f"The result is {result}")
finally:
    print("Execution finished.")
```

### Custom Exceptions

You can define your own exceptions by creating a new class that inherits from the built-in `Exception` class.

**Creating and Raising a Custom Exception:**

```python
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

try:
    raise CustomError("This is a custom exception")
except CustomError as e:
    print(f"Custom exception caught: {e}")
finally:
    print("Execution finished.")
```

**Example of Using Custom Exceptions in a Real-World Scenario:**

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.message = f"Attempted to withdraw {amount}, but only {balance} available."
        super().__init__(self.message)

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

# Creating a bank account object with a balance of 100
account = BankAccount(100)

try:
    account.withdraw(150)
except InsufficientFundsError as e:
    print(f"Error: {e}")
finally:
    print(f"Current balance: {account.balance}")
```

In this example, the `InsufficientFundsError` is a custom exception that is raised when an attempt is made to withdraw more money than is available in the bank account.


NumPy (Numerical Python) is a fundamental package for numerical computations in Python. It provides support for arrays, matrices, and many mathematical functions to operate on these data structures efficiently. Here's an overview of some of the core functionalities of NumPy:

### Installation

First, you need to install NumPy. If you haven't already, you can install it using pip:

```bash
pip install numpy
```

## Working with Libraries
---------------------------

### Importing NumPy

```python
import numpy as np
```

**Creating Arrays**

1. **From Lists**:

```python
import numpy as np

# 1D array
arr = np.array([1, 2, 3, 4])
print(arr)  # Output: [1 2 3 4]

# 2D array
arr_2d = np.array([[1, 2], [3, 4]])
print(arr_2d)  # Output: [[1 2]
              #          [3 4]]
```

2. **Using Built-in Functions**:

```python
# Array of zeros
zeros = np.zeros((2, 3))
print(zeros)  # Output: [[0. 0. 0.]
              #          [0. 0. 0.]]

# Array of ones
ones = np.ones((2, 3))
print(ones)  # Output: [[1. 1. 1.]
              #          [1. 1. 1.]]

# Array of evenly spaced values
arange = np.arange(0, 10, 2)
print(arange)  # Output: [0 2 4 6 8]

# Array of evenly spaced values in a specified range
linspace = np.linspace(0, 1, 5)
print(linspace)  # Output: [0.   0.25 0.5  0.75 1.  ]

```

3. **Random Arrays**:

```python
# Array with random values between 0 and 1
random = np.random.rand(2, 3)
print(random)  # Output: [[0.71518937 0.54488318 0.4236548 ]
              #          [0.64589411 0.43758721 0.891773  ]]

# Array with random integers
randint = np.random.randint(0, 10, (2, 3))
print(randint)  # Output: [[9 3 7]
               #          [2 7 2]]
```

### Array Operations

1. **Element-wise Operations**:

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Addition
print(a + b)  # Output: [5 7 9]

# Subtraction
print(a - b)  # Output: [-3 -3 -3]

# Multiplication
print(a * b)  # Output: [4 10 18]

# Division
print(a / b)  # Output: [0.25 0.4  0.5 ]
```

2. **Matrix Operations**:

```python
# Dot product
dot_product = np.dot(a, b)
print(dot_product)  # Output: 32

# Matrix multiplication
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

matrix_mult = np.matmul(matrix_a, matrix_b)
print(matrix_mult)  # Output: [[19 22]
                   #          [43 50]]
```

3. **Universal Functions (ufuncs)**:

```python
# Square root
sqrt = np.sqrt(a)
print(sqrt)  # Output: [1.         1.41421356 1.73205081]

# Exponential
exp = np.exp(a)
print(exp)  # Output: [ 2.71828183  7.3890561  20.08553692]

# Trigonometric functions
sin = np.sin(np.pi / 2)
print(sin)  # Output: 1.0
```

**Array Manipulation**

1. **Reshaping Arrays**:

```python
arr = np.arange(6)
reshaped = arr.reshape((2, 3))
print(reshaped)  # Output: [[0 1 2]
                #          [3 4 5]]
```

2. **Flattening Arrays**:

```python
flattened = reshaped.flatten()
print(flattened)  # Output: [0 1 2 3 4 5]
```

3. **Transposing Arrays**:

```python
transpose = reshaped.T
print(transpose)  # Output: [[0 3]
                  #          [1 4]
                  #          [2 5]]
```

**Slicing and Indexing**

```python
arr = np.array([1, 2, 3, 4, 5])

# Slicing
print(arr[1:4])  # Output: [2 3 4]

# Indexing
print(arr[2])  # Output: 3

# Conditional Slicing
print(arr[arr > 3])  # Output: [4 5]
```

**Statistical Operations**

```python
arr = np.array([1, 2, 3, 4, 5])

# Sum
print(arr.sum())  # Output: 15

# Mean
print(arr.mean())  # Output: 3.0

# Standard Deviation
print(arr.std())  # Output: 1.4142135623730951

# Max and Min
print(arr.max())  # Output: 5
print(arr.min())  # Output: 1
```

**Broadcasting**

Broadcasting allows NumPy to perform operations on arrays of different shapes.

```python
a = np.array([1, 2, 3])
b = np.array([[1], [2], [3]])

# Broadcasting addition
result = a + b
print(result)  # Output: [[2 3 4]
               #          [3 4 5]
               #          [4 5 6]]
```

**Example: Using NumPy for Numerical Computations**

```python
# Solving a system of linear equations
# 2x + 3y = 5
# 3x + 4y = 7

coefficients = np.array([[2, 3], [3, 4]])
constants = np.array([5, 7])

solution = np.linalg.solve(coefficients, constants)
print(solution)  # Output: [1. 1.]
```

