# AIRBNB CLONE PROJECT @ ALX SE.

The Airbnb clone is a copy of the Airbnb site where people can have access to
houses of private owners to lodge in. the application a description of all the
**amenities** provided by each house and the **price per night** in logding in any of
houses.

The goal of the project to to deploy a simple copy of the Airbnb website on my Local server. So for this purpose the Project has been divided in parts to aid smooth learning of the several and different intricacies in deployment a complete web application.

The project is divided into;
1. A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
2. A website (the front-end) that shows the final product to everybody: static and dynamic.
3. A database or files that store data (data = objects)
4. An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## The Command Intepreter
The command interpreter will serve as a gateway into our project. It's a crucial tool that helps us test the different tool we will be creating. so Basically the _Command Interpreter_ stage architecture of this project will consist of 2 components; _The storage engine_ and _The Console_. The console serves as a testing tool for us to experiment with and validate our storage engine. while the storage engine will apply the principles of serialisation and deserialisation to handle the data of the system while ensuring **Persistency**. 

_key file system structure are as follows_
```
\.AirBnB_clone
    console.py
    \.models
        basemodel.py
        city.py
        \.engine
            file_storage.py
``` 

### Starting the console
Like i mentioned previously the console is the gateway to all the functionalities of this Project.
On the parent pakage run the _console.py_ file.
this takes you to the console handling all the properties and functionalities of this program. and with this you are welcomed to our own small command interpreter world.

### Using the interpreter.
once logged into the console of this project you can directly begin all the process needed for manipulating the file storage system, with the right command.
_basic commands for the console include_;
`create`
`show`
`all`
`destroy`
`help`

### Some Quick Tips on using the various commands.
```
$ create BaseModel

$ show BaseModel 1234-1234-1234

$ destroy BaseModel 1234-1234-1234
```
 