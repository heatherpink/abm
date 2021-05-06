# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 18:08:20 2021

@author: Heather
"""
import random
import matplotlib
matplotlib.use('TkAgg')
import agentframework
import csv
import matplotlib.animation
import tkinter
import matplotlib.pyplot
import requests
import bs4
import sys

#Requests user to define number of agents.
try:
    num_of_agents = int(input("Enter number of agents: "))
except ValueError:
    print("Number of agents must be a number.")
    sys.exit() #Exits the application if an integer is not entered.

#Requests user to define number of iterations
try:
    num_of_iterations = int(input("Enter number of iterations: "))
except ValueError:
    print("Number of iterations must be a number.")
    sys.exit() #Exits the application if an integer is not entered.
    
agents = []
neighbourhood = 20
carry_on = True



#Import x and y values
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
#print(td_ys) #Can be used to test data has imported correctly
#print(td_xs) #Can be used to test data has imported correctly



#Calculates the distance between each agent
def distance_between(agents_row_a, agents_row_b):
    """
    Calculates the distance between two agents.

    Parameters
    ----------
    agents_row_a : list
        First agent in calculation
    agents_row_b : list
        Second agent in calculation

    Returns
    -------
    int
        The calculated distance between two agents

    """
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5



#Creating blank figure to map model on
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])



#Importing raster data, creating 2d list to construct map
with open("in.txt") as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    environment = []
   
    for row in reader: 
        rowlist = []
        environment.append(rowlist)
        for value in row:
            rowlist.append(value)
  
    
#Can be used to display initial environment 
# matplotlib.pyplot.imshow(environment)
# matplotlib.pyplot.show()   


      
# Creates each agent using the imported x and y data
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, y, x, agents))
#print(agents[0].agents[1]) #Can be used to test agents correctly contain a
                            #list of other agents



# Move the agents.
def update(frame_number):
    """
    Runs the agent-based model.
    
    The agents will move around the environment and as they move they will
    consume the environment and add this to their store. If two agents move 
    into the same neighbourhood their stores will be shared equally between 
    them. THe order in which the agents move will be randomised.
    This will continue until the agents store reaches the defined level or the
    number of iterations has been reached.

    Parameters
    ----------
    frame_number : list
        The frames used within the animation.

    Returns
    -------
    None.

    """
    fig.clear()
    global carry_on
    
    for i in range(num_of_agents):
        random.shuffle(agents) #shuffle the list of agents each time
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        #print(agents[i].store) #Can be used to test store is increasing and
                                #being shared correctly
       
        
    for k in range(num_of_agents):
        fig.clear()
        matplotlib.pyplot.xlim(0, 99)
        matplotlib.pyplot.ylim(0, 99)
        matplotlib.pyplot.imshow(environment)
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
        #print(agents[i].x, agents[i].y) #Can be used to test agents are moving
                                         #correctly
    
    
    #Defines a stopping condition where the model stops once the agent's store
    #reaches 1000
    if agents[i].store > 1000:
        carry_on = False
        print("stopping condition")



#Defines a stopping condition where the model stops once the defined number of
#iterations has been reached        
def gen_function():
    """
    Defines the stopping condition of the model.
    
    The stopping condition will be reached when the number of iterations has 
    been reached. This is in addition to the limit on the agent's store.

    Yields
    ------
    a : TYPE
        DESCRIPTION.

    """
    a = 0
    global carry_on
    while (a < num_of_iterations) & (carry_on) :
        yield a
        a = a + 1



def run():
    """
    Runs the animation of the model.

    Returns
    -------
    None.

    """
    animation = matplotlib.animation.FuncAnimation(fig, update, 
                frames=gen_function, repeat=False)
    canvas.draw()



#Creates a window that the animation runs within
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)



#Creates a menu bar with the option to run the model
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
tkinter.mainloop()

