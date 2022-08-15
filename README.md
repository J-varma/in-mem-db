# in-mem-db
In Memory Database - A popular assignment question I found Interesting.
## Problem Statement:
### Programming Assignment: Simple Database
Implement an in-memory database. Your program will receive commands via standard input (stdin) and should write appropriate responses to standard output (stdout). You can use high-level languages such as Python, Ruby, Java, C#, …, etc.

Your database should accept the following commands:

**SET name value** – Set the variable name to the value. Neither variable names nor values will contain spaces.

**GET name** – Print out the value of the variable name, or NULL if that variable is not set. 

**UNSET name** – Unset the variable name, making it just like that variable was never set. 

**NUMEQUALTO value** – Print out the number of variables that are currently set to value. If no variables equal that value, print 0. 

**ADD name value** – Add the value to variable name, or NULL if that variable name is not set. 

**ADD name1 name2** – Add the value of variable name2 to variable name1, or NULL if that any variable name is not set. 

**END** – Exit the program. 

Your program will always receive this as its last command. Commands will be fed to your program one at a time, with each command on its own line. Any output that your program generates should end with a newline character.

Here are some example command sequences:

### INPUT&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;OUTPUT
SET x 10

GET x&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;10

UNSET x

GET x&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;NULL

END

---

### INPUT&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;OUTPUT

SET a 10

SET b 10

NUMEQUALTO 10&emsp;&emsp;&emsp;&emsp;&emsp;2

NUMEQUALTO 20&emsp;&emsp;&emsp;&emsp;&emsp;0

SET b 30

NUMEQUALTO 10&emsp;&emsp;&emsp;&emsp;&emsp;1

END

---

Transaction Commands In addition to the above data commands, your program should also support database transactions by also implementing these commands:

**BEGIN** – Open a new transaction block. Transaction blocks can be nested; a BEGIN can be issued inside of an existing block.

**ROLLBACK** – Undo all of the command’s issues in the most recent transaction block, and close the block. Print nothing if successful or print **NO TRANSACTION** if no transaction is in progress.

**COMMIT** – Close all open transaction blocks, permanently applying the changes made in them. Print nothing if successful or print NO TRANSACTION if no transaction is in progress. Any data command that is run outside of a transaction block should commit immediately.

Here are some example command sequences:

---

### INPUT&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;OUTPUT
BEGIN

SET a 10

GET a&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;10

BEGIN

SET a 20

GET a&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;20

ROLLBACK

GET a&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;10

ROLLBACK

GET a&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;NULL

END

---

### INPUT&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;OUTPUT
BEGIN

SET a 30

BEGIN

SET a 40

COMMIT

GET a&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;40

ROLLBACK&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;NO TRANSACTION

END
