#GitHub - https://github.com/JHill-Harding/Earthwave_CV
import os,time
class Applicant:
    role = "Junior Software Engineer"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def gloat(self):
        print("I have 2 Years of Python Experience,")
        print("As well as 6 Months of SQL database querying." + '\n')
    def reassure(self):
        explain = {
            "GitHub":"I am aware of power, but have no formal experince. I am used to custom Excel dashboard and paper tracking.",
            "Data Analysis":"I have experience of data analysis and writing code to interpret data for product devolpment and statistics for managment.",
            "Unity Game Engine":"Many years ago, I dabbled with Unity for game devoplment as a past time for fun."}
        return explain

Josh=Applicant("Joshua",23)
print('\n' + "My name is Joshua and I am applying for the {} position.".format(Josh.__class__.role) + '\n')
Josh.gloat()
print("GitHub - " + Josh.reassure()['GitHub'])
print("Data Analysis - " + Josh.reassure()['Data Analysis'])
print("Unity Game Engine - " + Josh.reassure()['Unity Game Engine'] + '\n')

d={}
d[0] = "I would love to work for Earthwave as I belive the work they are doing can be key to helping"
d[1] = "inform the general population about climate change and the warming of our world."
d[2] = "I would also like to start to develop my software writing skills further, which I belive Earthwave can help me do."
d[3] = "I find it very rewarding and fun to figure out new ways of handling data and automating tasks,"
d[4] = "for example I learnt python so I could write a program with a GUI to standardize the calculation and graphs from a test, as this allows "
d[5] = "multiple users to access and use it. This was a key part of the design as most scripts/calculators used by my company are written with either"
d[6] = "NI LabVIEW or Visual Basic (Excel) which will have issues if multiple instances are open at a time, not to mention they can be very slow/resource hungry." + '\n'
for i in range(6):
    print(d[i])
input("Press Enter to continue...")

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
              @@@@@@         
""")
globe2 = (r"""
              @@@@@@
	    @@...  ..@@
	  @@.../      @@
	 @  \./      /..@
	@  /...\_    |...@
	@ /......\    \./@
	@ \......|       @
	 @ \..../       @
	  @@\../      @@
            @@  ... @@
             @@@@@@
           """)
globe3 = (r"""
	      @@@@@@
	    @@	 ...@@
	  @@    /...__@@
	 @     /.../    @
	@      \..|___   @
	@  .    \.....\  @
	@        \..../  @
	 @        |../  @
	  @@   .  \./ @@
            @@ ..   @@
     	      @@@@@@
           """)
globe4 = (r"""
	      @@@@@@
	    @@......@@
	  @@         /@@
	 @ 	     \..@
	@             \..@
	@        .     \.@
	@\              \@
	 @\            . @
	  @@\         @@
	    @@.     @@
     	      @@@@@@
           """)
os.system('cls')
globes = [globe1,globe2,globe3,globe4]
def animator(globes, delay = 0.1, repeat = 10):
    frames = []
    for image in globes:
        frames.append(image)
    for i in range(repeat):
        for frame in frames:
            print("".join(frame))
            time.sleep(delay)
            os.system('cls')
animator(globes,delay=0.2,repeat=10)