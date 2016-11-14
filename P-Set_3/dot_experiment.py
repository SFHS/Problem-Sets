from psychopy import core, visual, event
from numpy import random
import json
win = visual.Window(size=(1600,900), color='gray', units='pix')

# General setup
numTrials = 2
fixationTime = 1
responseVector = [];
dotTimeVector=[];
isDotTrial = random.choice(range(numTrials), size=numTrials/2, replace=False)

# Trial loop
for i in range(numTrials):
    # Random time between cross and dot
    jitterTime = random.uniform(0.5,1)
    # Random dot time 
    dotTime = random.uniform(0.05,0.2)
    dotTimeVector.append(dotTime)
    
    # Define and draw fixation cross
    fixationCross = visual.TextStim(win, color='#FFFFFF', text = "+", units='norm', height=0.1, alignHoriz='center', alignVert='center')
    fixationCross.draw()
    # Show fixation cross
    win.flip()
    # Wait for fixation time
    core.wait(fixationTime)
    # Remove fixation cross
    win.flip()
    # Wait for random jittered time until dot
    core.wait(jitterTime)
    # Plot white dot IF IT IS A DOT TRIAL:
    dot = visual.Circle(win, radius=1, edges=32, fillColor=(10,10,10), fillColorSpace='rgb255')
    # Check if this is a trial with a dot
    if i in isDotTrial:
        dot.draw()
    win.flip()
    # Wait for the randomized dot time
    core.wait(dotTime)
    # Remove dot from the screen
    win.flip()
    # Wait a little bit more without the dot
    core.wait(1-dotTime)
    # Draw and display green square for response
    square = visual.Rect(win, width=50, height=50, fillColor=(0,255,0), fillColorSpace='rgb255')
    square.draw()
    win.flip()
    # Wait for response
    k = ['']
    while k[0] not in ['left', 'right']:
        k = event.waitKeys()
        responseVector.append(k)
    # END OF FOR LOOP

# Saving results to a file
f = open('datafile.txt', 'w')
# JSON allows you to save the full vector to the file by using dump (yes, dump!)
json.dump(responseVector, f) # Saving responses to file
json.dump(isDotTrial.tolist(), f) # Saving trial identifiers to file
json.dump(dotTimeVector, f) # Saving randomized dot time to file

win.close()
core.quit()