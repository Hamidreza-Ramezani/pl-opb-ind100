import random as rd
import pandas as pd
import sympy as sp
import prairielearn as pl
import problem_bank_helpers as pbh
import math

def imports(data):
    import random as rd
    import pandas as pd
    import sympy as sp
    import prairielearn as pl
    import problem_bank_helpers as pbh
    import math
    
def generate(data):
    data2 = pbh.create_data2()
    
    data2["params"]["vars"]["title"] = "National Health Plan, Part II"
    
    # Generate random data
    p_hat = round(rd.uniform(0.4, 0.7), 1)  # Support proportion
    margin_of_error = 0.01  # Fixed margin of error
    z_score = rd.choice([1.6449, 1.96, 2.3263])  # Z-score for different confidence levels (90%, 95%, 98%)
    confidence = {1.6449: 90, 1.96: 95, 2.3263: 98}[z_score]  # Confidence level
    
    # Calculate the standard error (SE) using the formula for sample size calculation
    n = math.ceil((z_score**2 * p_hat * (1 - p_hat)) / margin_of_error**2)
    p_hat_percent = p_hat*100
    margin_of_error_percent = margin_of_error*100
    
    # Store these variables in the data dictionary to use them later
    data2['params']['vars']['p_hat'] = p_hat
    data2['params']['vars']['p_hat_percent'] = p_hat_percent
    data2['params']['vars']['margin_of_error_percent'] = margin_of_error_percent
    data2['params']['vars']['z_score'] = z_score
    data2['params']['vars']['confidence'] = confidence
    data2['params']['vars']['n'] = n
    data2['correct_answers']['part1_ans'] = n
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass
    
