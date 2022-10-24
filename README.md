# demonstrationProject
Here is an example of a git respository. This is a readme file which will automatically be shown to anyone who looks at the project. Usefull information can be put here such as:
  - Guides on project setup
  - What the project is
  - How to use the project

In this example, I have produced a python program that very basically models vehicles. The basic requirements were:
  - All vehicles must be able to drive
  - All vehicles must have the following attributes:
    - An engine size between 0 - 9999cc
    - A fuel type of petrol, diesel or electric
    - A number of seats in the range of 0 to 20
  - There will be 3 types of vehicles: Vans, cars and motorbikes
    - Motorbikes must have a wheelie function and an attribute representing if it can or can't wheelie
    - Vans must have a payload ranging from 0 to 1999kg 

This code has been properly wrote, tested and commented. Furthermore, I have used Sphinx to produce HTML documentation.

Tasks you can do:
  - Pull this project to your system and make a new branch
  - Fill out the Lorry class, It should contain the following
    - A variable representing if the Lorry is carrying a trailer
    - A variable representing the length of the Lorry. It should be between 4000 and 18750
    - An __init__() method that creates a Lorry object
    - A dock function that should dock a trailer if there is no trailer and undock if it is
  - Once this is done you can write some test cases. Remember that:
    - All branches should be tested
    - You should test the boundaries of all the variables
  - Afterwards you should push your changes to git. There I can view them and provide feedback.
