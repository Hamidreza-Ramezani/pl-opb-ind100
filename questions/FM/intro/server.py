import random
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()
    
    # store phrases etc
    data2["params"]["vars"]["title"] = "Intro-Instructor"
    data2["params"]["vars"]["course"] = "Data 301"
    
    # Randomize Variables
    names = [
        "Dr. Nancy Pelosi",
        "Dr. Daniel Shiffman",
        "Dr. Jonathan Thomas-Palmer",
        "Dr. Donald Trump",
        "Dr. Shini Somara",
        "Dr. Sheldon Cooper",
        "Dr. Donna Strickland",
        "Dr. Rosalind Franklin",
        "Dr. Isaac Newton",
    ]
    
    for i, nm in enumerate(random.sample(names, 5)):
        data2["params"]["part1"][f"ans{i+1}"]["value"] = nm
        data2["params"]["part1"][f"ans{i+1}"]["correct"] = False
    
    data2["params"]["part1"][f"ans{i+2}"]["value"] = "Dr. Firas Moosvi"
    data2["params"]["part1"][f"ans{i+2}"]["correct"] = True
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass