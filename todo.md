
### Example

X (A) 2023-10-09 2023-15-09 create python todo.txt +learning_programming @project due:2023-18-09

### Rules
X - marks completion
(A) - marks priority
first date - marks completion date
second date - marks creation date
text - describes task
+ - describes project
@ - describes context - context means place and situation that you'll work on the task
due + date - describes due date


### Commands
- add "" -> this command adds tasks
- list || ls -> this command lists tasks
	- ls +learning_programming
	- ls @project
	- ls create
- list || ls can be compounded
	- ls +learning_programming @project


### Approach
- my file can either be a json file or text file
	- text file can take up less space and be less verbose
	- json file can hold up a lot of information intuitivly but take up a lot of lines + become verbose
- probably should try with .txt and then create another version that works with json file as well


### Progress
- Implemented basic logic of the program
- Implemented basic commands
	- add task
	- list tasks
	- create compounded list tasks command

### TODO
[x] - list tasks with index numbers
- need to create functionality that selects a task
- this is needed in order to mark task as complete
- edit task
- list just incomplete tasks
- change priority
