print(__name__) # module to run first point of excution

""" 
1- They are two modules name demo and calc 
2- when you are working on demo and print(__name__ )
Output- _main_(because it is starting point of a code)
3- Now we will work on calc and print hello __name__
Output- hello main 
This is happening and it is giving name as main output because we are working on same module 

Now when we import one module to other ( import calc to demo)
1- All the things in calc will be printed along with demo statements
2- but it will print hello calc (the module name )
Instead of hello main 
Because we are importing it to other module 
"sooo when you are importing it in same module it will give name output as main 

And if in other module it will give name output along with module name...... that's it """


"""When we define a function, then we will have to call that function also to print or perform something.
main() is the starting point of execution.
main() function will also work only when we call the main() function. 
From the main() function, we can call all other functions that are available in the code.
When you import the library or a module, it will execute all statements present inside it.
And if it contains the callable main() function, then main() will call all functions present in the imported module.
We can also call the main() function only when we want to execute the particular file as a Standalone program.
We can control the execution flow of main() by using:
 if _ name_  == _main()_
So by using this, some set of statements will be executed only when we call the __name__."""