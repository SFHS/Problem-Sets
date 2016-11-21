# ========================== 
# RTdemo.py 
""" 
ask a question, 
get a keystoke 
measure reaction time 
""" 
from psychopy import visual, event, core 
from random import random 

#create a window to draw in 
wintype='pyglet' # use pyglet if possible, it's faster at event handling 
myWin = visual.Window((600.0,600.0),allowGUI=False,winType=wintype) 

sans = ['Gill Sans MT', 'Arial','Helvetica','Verdana'] #use the first font found on this list 
ask4key=visual.TextStim(myWin, text='Press a key as fast as you can RIGHT NOW!',font=sans, units='norm', height=.10,pos=(-.95,0),alignHoriz='left') 

RT = core.Clock() # make a clock for capturing RT (reaction time) 

while True: # replace the .... 's with spaces or a tab 
    # clear any keystrokes before starting 
    event.clearEvents() 
    allKeys=[] 

    # paint the stimulus to react to: 
    ask4key.draw() 
    myWin.flip() 
    RT.reset() # reaction time starting immediately after flip 

    while len(allKeys)==0: # wait for a keypress 
        allKeys=event.getKeys(timeStamped=RT) 
        # see the online PsychoPy reference manual on event.getKeys for details of use and code 
        # if timeStamped = a core.Clock object, it causes return of the tuple (key,time-elapsed-since-last-reset) 

    # now allKeys is [(key, milliseconds)] 
    # if you don't have pyglet, you need to get the time explicitly 
    if not wintype == 'pyglet': 
        allKeys[0][1] = RT.getTime() 

    # unpack allKeys  taking the first keypress in the list 
    thekey=allKeys[0][0].upper() 
    theRT =allKeys[0][1] 

    if thekey =='ESCAPE': core.quit() 

    if theRT < 0.5 : feedback="Pretty fast! Now wait for it..." 
    else: feedback="You can do better. C'mon now! ready....and ..." 
    msg="Your reaction time was %5.4f seconds. %s"%(theRT,feedback) 
    ask4key.setText(msg) 
    ask4key.draw() 
    myWin.flip() 

    ask4key.setText('Press a key as fast as you can RIGHT NOW!') 
    # wait for 3-8 seconds to read feedback and have uncertain wait time before next trial 
    core.wait(3+int(random()*6)) 