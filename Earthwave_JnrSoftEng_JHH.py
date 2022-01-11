# V1.0 - Written by Joshua Hill-Harding for Earthwave job application
# GitHub - https://github.com/JHill-Harding/Earthwave_CV
import os,time                              # import OS and Time, These are always default included in python install so shouldn't cause issues.
class Applicant:                            # This is to show some knowledge of Object Orientated Programming
    role = "Junior Software Engineer"       # Class attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def gloat(self):                        # Instance 1 - Gloating about a core Skill - Simple prints when called
        print("I have 2 Years of Python Experience,")
        print("As well as 6 Months of SQL database querying." + '\n')
    def reassure(self):                     # Instance 2 - Explaining about how I have an idea or other experiences 
        explain = {                         # Dictionary because why not? 
            "GitHub":"I am aware of power, but have no formal experience. I am used to custom Excel dashboard and paper tracking.",
            "Data Analysis":"I have experience of data analysis and writing code to interpret data for product development and statistics for management.",
            "Unity Game Engine":"Many years ago, I dabbled with Unity for game development as a past time for fun."}
        return explain

Josh=Applicant("Joshua",23)                 # Assign Josh with a name and age 
print('\n' + "My name is Joshua and I am applying for the {} position.".format(Josh.__class__.role) + '\n')
Josh.gloat()                                # Call Gloat for Josh 
print("GitHub - " + Josh.reassure()['GitHub'])
print("Data Analysis - " + Josh.reassure()['Data Analysis'])
print("Unity Game Engine - " + Josh.reassure()['Unity Game Engine'] + '\n')

d={}                                        # Big wall of text, want to print all so use dictionary and loop to save space/lines.
d[0] = "I would love to work for Earthwave as I believe the work they are doing can be key to helping"
d[1] = "inform the general population about climate change and the warming of our world."
d[2] = "I would also like to start to develop my software writing skills further, which I believe Earthwave can help me do."
d[3] = "I find it very rewarding and fun to figure out new ways of handling data and automating tasks,"
d[4] = "for example I learnt python so I could write a program with a GUI to standardize the calculation and graphs from a test, as this allows "
d[5] = "multiple users to access and use it. This was a key part of the design as most scripts/calculators used by my company are written with either"
d[6] = "NI LabVIEW or Visual Basic (Excel) which will have issues if multiple instances are open at a time, not to mention they can be very slow/resource hungry." + '\n'
for i in d:                                 # For all values in d (items in d)
    print(d[i])                             # Print from list d item I

input("Press Enter to continue...")         # Wait for user to click Enter to continue

# Bit of fun animation - Would use PIL and byte array images but i dont have enough lines and don't want to import extra packages
globe1 = (r"""
          @@@@@@        
        @@... /.@@      
      @@     /....@@    
     @      /.......@   
    @.\     |........@  
    @..\     \./ \...@  
    @...\        |...@  
     @...|       |..@   
      @@/         @@    
        @@...   @@ 
          @@@@@@         """)
globe2 = (r"""
          @@@@@@
        @@... ..@@
      @@.../      @@
     @  \./      /..@
    @  /...\_    |...@
    @ /......\    \./@
    @ \......|       @
     @ \..../       @
      @@\../      @@
        @@  ... @@
          @@@@@@		""")
globe3 = (r"""
          @@@@@@
        @@   ...@@
      @@    /...__@@
     @     /.../    @
    @      \..|___   @
    @  .    \.....\  @
    @        \..../  @
     @        |../  @
      @@   .  \./ @@
        @@ ..   @@
          @@@@@@		""")
globe4 = (r"""
          @@@@@@
        @@......@@
      @@         /@@
     @       \..@
    @             \..@
    @        .     \.@
    @\              \@
     @\            .@
      @@\         @@
        @@.     @@
          @@@@@@		""")

os.system('cls')                                    # Clear the terminal
globes = [globe1,globe2,globe3,globe4]              # Set Globe attributes
def animation(globes, delay, repeat):               # Define my animation function
    for i in range(repeat):                         # Run code 'repeat' times 
        for frame in globes:
            print("".join(frame))                   # Print the 'image' 
            time.sleep(delay)                       # Delay before continue
            os.system('cls')                        # Clear terminal for next 'image'
animation(globes, delay = 0.2, repeat = 10)         # Run Function->Animation, with globes input, a delay of 200ms and repeat it 10 times 