#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2025.1.1),
    on Wed Nov 12 12:39:31 2025
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2025.1.1'
expName = 'manipulation-of-belief'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1440, 900]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/francesco/Documents/dev/02455-Experiment-In-Cognitive-Science/manipulation-of-belief_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=True, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units=None,
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = None
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    if deviceManager.getDevice('key_instruct') is None:
        # initialise key_instruct
        key_instruct = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_instruct',
        )
    if deviceManager.getDevice('rating_sam_1') is None:
        # initialise rating_sam_1
        rating_sam_1 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='rating_sam_1',
        )
    if deviceManager.getDevice('rating_sam_2') is None:
        # initialise rating_sam_2
        rating_sam_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='rating_sam_2',
        )
    if deviceManager.getDevice('rating_sam_3') is None:
        # initialise rating_sam_3
        rating_sam_3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='rating_sam_3',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "r_instructions" ---
    instructions_text = visual.TextStim(win=win, name='instructions_text',
        text="You’ll watch four short, content-friendly videos where each one has a label that either says “AI-generated” or “human-generated”.\n\nAfter each video, you’ll fill out a short questionnaire about your experience with this video.\n \nYou can stop and withdraw at any time if you feel uncomfortable or simply don’t want to continue.\n\nPress SPACE when you're ready.",
        font='Arial',
        units='norm', pos=(0, 0), draggable=False, height=0.1, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_instruct = keyboard.Keyboard(deviceName='key_instruct')
    # Run 'Begin Experiment' code from text_align
    # Code components should usually appear at the top
    # of the routine. This one has to appear after the
    # text component it refers to.
    instructions_text.alignText= 'left'
    
    # --- Initialize components for Routine "r_baseline" ---
    baseline_countdown = visual.TextStim(win=win, name='baseline_countdown',
        text='',
        font='Arial',
        units='norm', pos=(0, -0.5), draggable=False, height=0.1, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    baseline_text = visual.TextStim(win=win, name='baseline_text',
        text='Please now wait still and relax while we measure the baseline for your heartbeat at rest.\n\nOnly good vibes :)',
        font='Arial',
        units='norm', pos=(0, 0), draggable=False, height=0.1, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    # Run 'Begin Experiment' code from text_align_2
    # Code components should usually appear at the top
    # of the routine. This one has to appear after the
    # text component it refers to.
    baseline_text.alignText= 'left'
    
    # --- Initialize components for Routine "r_preparation" ---
    # Run 'Begin Experiment' code from load_design
    import csv
    import time
    
    base_dir = os.path.dirname(__file__)
    
    csv_path = os.path.join(base_dir, 'variables', 'subjects_design.csv')
    
    stimuli_design = []
    with open(csv_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stimuli_design.append(row)
    
    subj_num = int(expInfo['participant'])
    selected_order = stimuli_design[subj_num]
    
    print(f"Subject {subj_num} - selected order: {selected_order}")
    
    thisExp.addData('expStartTime', time.time())
    video_nature_cue_text = visual.TextStim(win=win, name='video_nature_cue_text',
        text='',
        font='Arial',
        units='norm', pos=(0, 0), draggable=False, height=0.1, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "r_fixation" ---
    fixation_cross = visual.ShapeStim(
        win=win, name='fixation_cross', vertices='cross',
        size=(30,30),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor=[-0.1765, -0.1765, -0.1765],
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "r_video" ---
    video = visual.MovieStim(
        win, name='video',
        filename=None, movieLib='ffpyplayer',
        loop=False, volume=1.0, noAudio=False,
        pos=(0, 0), size=(2.0,2.0), units='norm',
        ori=0.0, anchor='center',opacity=None, contrast=1.0,
        depth=0
    )
    
    # --- Initialize components for Routine "r_SAM_1" ---
    question_sam_1_text = visual.TextStim(win=win, name='question_sam_1_text',
        text='Press a button 1-5 to express how the last video made you feel about being \nunhappy / happy\n\n(1 = very unhappy, 5 = very happy)',
        font='Arial',
        units='norm', pos=(0, 0.5), draggable=False, height=0.1, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    question_sam_1 = visual.ImageStim(
        win=win,
        name='question_sam_1', units='norm', 
        image='stimuli/sam-1.png', mask=None, anchor='center',
        ori=0.0, pos=(0,-0.3), draggable=False, size=(1.3,0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    rating_sam_1 = keyboard.Keyboard(deviceName='rating_sam_1')
    
    # --- Initialize components for Routine "r_SAM_2" ---
    question_sam_2_text = visual.TextStim(win=win, name='question_sam_2_text',
        text='Press a button 1-5 to express how the last video made you feel about being \ncalm / excited\n\n(1 = very calm, 5 = very excited)',
        font='Arial',
        units='norm', pos=(0, 0.5), draggable=False, height=0.1, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    question_sam_2 = visual.ImageStim(
        win=win,
        name='question_sam_2', units='norm', 
        image='stimuli/sam-2.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.3), draggable=False, size=(1.3,0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    rating_sam_2 = keyboard.Keyboard(deviceName='rating_sam_2')
    
    # --- Initialize components for Routine "r_SAM_3" ---
    question_sam_3_text = visual.TextStim(win=win, name='question_sam_3_text',
        text='Press a button 1-5 to express how the last video made you feel about being \ncontrolled / incontrolled\n\n(1 = very controlled, 5 = very incontrolled)',
        font='Arial',
        units='norm', pos=(0, 0.5), draggable=False, height=0.1, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    question_sam_3 = visual.ImageStim(
        win=win,
        name='question_sam_3', units='norm', 
        image='stimuli/sam-3.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.3), draggable=False, size=(1.3,0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    rating_sam_3 = keyboard.Keyboard(deviceName='rating_sam_3')
    
    # --- Initialize components for Routine "r_focus_questionnaire" ---
    focus_text = visual.TextStim(win=win, name='focus_text',
        text='In general, how focused were you about what was happening on the screen when watching the previous video?',
        font='Arial',
        units='norm', pos=(0, 0.5), draggable=False, height=0.1, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    focus_slider = visual.Slider(win=win, name='focus_slider',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units='norm',
        labels=['Not focused at all','','','','Very focused'], ticks=(1, 2, 3, 4, 5), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-1, readOnly=False)
    
    # --- Initialize components for Routine "r_final_questionnaire" ---
    opinion_text = visual.TextStim(win=win, name='opinion_text',
        text='In general, what is your opinion on AI-generated visual contents (specifically AI-generated videos)?',
        font='Arial',
        units='norm', pos=(0, 0.5), draggable=False, height=0.1, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    opinion_slider = visual.Slider(win=win, name='opinion_slider',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units='norm',
        labels=['I don\'t like them','','','','I really like them'], ticks=(1, 2, 3, 4, 5), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-1, readOnly=False)
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "r_instructions" ---
    # create an object to store info about Routine r_instructions
    r_instructions = data.Routine(
        name='r_instructions',
        components=[instructions_text, key_instruct],
    )
    r_instructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_instruct
    key_instruct.keys = []
    key_instruct.rt = []
    _key_instruct_allKeys = []
    # store start times for r_instructions
    r_instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    r_instructions.tStart = globalClock.getTime(format='float')
    r_instructions.status = STARTED
    thisExp.addData('r_instructions.started', r_instructions.tStart)
    r_instructions.maxDuration = None
    # keep track of which components have finished
    r_instructionsComponents = r_instructions.components
    for thisComponent in r_instructions.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "r_instructions" ---
    r_instructions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_text* updates
        
        # if instructions_text is starting this frame...
        if instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_text.frameNStart = frameN  # exact frame index
            instructions_text.tStart = t  # local t and not account for scr refresh
            instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            instructions_text.status = STARTED
            instructions_text.setAutoDraw(True)
        
        # if instructions_text is active this frame...
        if instructions_text.status == STARTED:
            # update params
            pass
        
        # *key_instruct* updates
        waitOnFlip = False
        
        # if key_instruct is starting this frame...
        if key_instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_instruct.frameNStart = frameN  # exact frame index
            key_instruct.tStart = t  # local t and not account for scr refresh
            key_instruct.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_instruct, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_instruct.started')
            # update status
            key_instruct.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_instruct.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_instruct.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_instruct.status == STARTED and not waitOnFlip:
            theseKeys = key_instruct.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_instruct_allKeys.extend(theseKeys)
            if len(_key_instruct_allKeys):
                key_instruct.keys = _key_instruct_allKeys[0].name  # just the first key pressed
                key_instruct.rt = _key_instruct_allKeys[0].rt
                key_instruct.duration = _key_instruct_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=r_instructions,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            r_instructions.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in r_instructions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "r_instructions" ---
    for thisComponent in r_instructions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for r_instructions
    r_instructions.tStop = globalClock.getTime(format='float')
    r_instructions.tStopRefresh = tThisFlipGlobal
    thisExp.addData('r_instructions.stopped', r_instructions.tStop)
    # check responses
    if key_instruct.keys in ['', [], None]:  # No response was made
        key_instruct.keys = None
    thisExp.addData('key_instruct.keys',key_instruct.keys)
    if key_instruct.keys != None:  # we had a response
        thisExp.addData('key_instruct.rt', key_instruct.rt)
        thisExp.addData('key_instruct.duration', key_instruct.duration)
    thisExp.nextEntry()
    # the Routine "r_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "r_baseline" ---
    # create an object to store info about Routine r_baseline
    r_baseline = data.Routine(
        name='r_baseline',
        components=[baseline_countdown, baseline_text],
    )
    r_baseline.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for r_baseline
    r_baseline.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    r_baseline.tStart = globalClock.getTime(format='float')
    r_baseline.status = STARTED
    thisExp.addData('r_baseline.started', r_baseline.tStart)
    r_baseline.maxDuration = None
    # keep track of which components have finished
    r_baselineComponents = r_baseline.components
    for thisComponent in r_baseline.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "r_baseline" ---
    r_baseline.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *baseline_countdown* updates
        
        # if baseline_countdown is starting this frame...
        if baseline_countdown.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            baseline_countdown.frameNStart = frameN  # exact frame index
            baseline_countdown.tStart = t  # local t and not account for scr refresh
            baseline_countdown.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(baseline_countdown, 'tStartRefresh')  # time at next scr refresh
            # update status
            baseline_countdown.status = STARTED
            baseline_countdown.setAutoDraw(True)
        
        # if baseline_countdown is active this frame...
        if baseline_countdown.status == STARTED:
            # update params
            baseline_countdown.setText("{:02d}:{:02d}".format((120-int(t))//60, (120-int(t))%60), log=False)
        
        # if baseline_countdown is stopping this frame...
        if baseline_countdown.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > baseline_countdown.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                baseline_countdown.tStop = t  # not accounting for scr refresh
                baseline_countdown.tStopRefresh = tThisFlipGlobal  # on global time
                baseline_countdown.frameNStop = frameN  # exact frame index
                # update status
                baseline_countdown.status = FINISHED
                baseline_countdown.setAutoDraw(False)
        
        # *baseline_text* updates
        
        # if baseline_text is starting this frame...
        if baseline_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            baseline_text.frameNStart = frameN  # exact frame index
            baseline_text.tStart = t  # local t and not account for scr refresh
            baseline_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(baseline_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            baseline_text.status = STARTED
            baseline_text.setAutoDraw(True)
        
        # if baseline_text is active this frame...
        if baseline_text.status == STARTED:
            # update params
            pass
        
        # if baseline_text is stopping this frame...
        if baseline_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > baseline_text.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                baseline_text.tStop = t  # not accounting for scr refresh
                baseline_text.tStopRefresh = tThisFlipGlobal  # on global time
                baseline_text.frameNStop = frameN  # exact frame index
                # update status
                baseline_text.status = FINISHED
                baseline_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=r_baseline,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            r_baseline.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in r_baseline.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "r_baseline" ---
    for thisComponent in r_baseline.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for r_baseline
    r_baseline.tStop = globalClock.getTime(format='float')
    r_baseline.tStopRefresh = tThisFlipGlobal
    thisExp.addData('r_baseline.stopped', r_baseline.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if r_baseline.maxDurationReached:
        routineTimer.addTime(-r_baseline.maxDuration)
    elif r_baseline.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    stimuli = data.TrialHandler2(
        name='stimuli',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('variables/stimuli.csv'), 
        seed=None, 
    )
    thisExp.addLoop(stimuli)  # add the loop to the experiment
    thisStimulus = stimuli.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisStimulus.rgb)
    if thisStimulus != None:
        for paramName in thisStimulus:
            globals()[paramName] = thisStimulus[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisStimulus in stimuli:
        stimuli.status = STARTED
        if hasattr(thisStimulus, 'status'):
            thisStimulus.status = STARTED
        currentLoop = stimuli
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisStimulus.rgb)
        if thisStimulus != None:
            for paramName in thisStimulus:
                globals()[paramName] = thisStimulus[paramName]
        
        # --- Prepare to start Routine "r_preparation" ---
        # create an object to store info about Routine r_preparation
        r_preparation = data.Routine(
            name='r_preparation',
            components=[video_nature_cue_text],
        )
        r_preparation.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from load_design
        video_file = os.path.join(base_dir, 'stimuli', selected_order[f'video{video_index}'])
        label_text = selected_order[f'label{video_index}']
        
        stimuli.addData('video_id', selected_order[f'video{video_index}'])
        stimuli.addData('belief', selected_order[f'label{video_index}'])
        # store start times for r_preparation
        r_preparation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        r_preparation.tStart = globalClock.getTime(format='float')
        r_preparation.status = STARTED
        thisExp.addData('r_preparation.started', r_preparation.tStart)
        r_preparation.maxDuration = None
        # keep track of which components have finished
        r_preparationComponents = r_preparation.components
        for thisComponent in r_preparation.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "r_preparation" ---
        r_preparation.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 5.0:
            # if trial has changed, end Routine now
            if hasattr(thisStimulus, 'status') and thisStimulus.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *video_nature_cue_text* updates
            
            # if video_nature_cue_text is starting this frame...
            if video_nature_cue_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                video_nature_cue_text.frameNStart = frameN  # exact frame index
                video_nature_cue_text.tStart = t  # local t and not account for scr refresh
                video_nature_cue_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(video_nature_cue_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                video_nature_cue_text.status = STARTED
                video_nature_cue_text.setAutoDraw(True)
            
            # if video_nature_cue_text is active this frame...
            if video_nature_cue_text.status == STARTED:
                # update params
                video_nature_cue_text.setText("The next video is going to be " + "\n" + str(label_text) + "\n\n" + str(5-int(t)), log=False)
            
            # if video_nature_cue_text is stopping this frame...
            if video_nature_cue_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > video_nature_cue_text.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    video_nature_cue_text.tStop = t  # not accounting for scr refresh
                    video_nature_cue_text.tStopRefresh = tThisFlipGlobal  # on global time
                    video_nature_cue_text.frameNStop = frameN  # exact frame index
                    # update status
                    video_nature_cue_text.status = FINISHED
                    video_nature_cue_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=r_preparation,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                r_preparation.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in r_preparation.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "r_preparation" ---
        for thisComponent in r_preparation.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for r_preparation
        r_preparation.tStop = globalClock.getTime(format='float')
        r_preparation.tStopRefresh = tThisFlipGlobal
        thisExp.addData('r_preparation.stopped', r_preparation.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if r_preparation.maxDurationReached:
            routineTimer.addTime(-r_preparation.maxDuration)
        elif r_preparation.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        
        # --- Prepare to start Routine "r_fixation" ---
        # create an object to store info about Routine r_fixation
        r_fixation = data.Routine(
            name='r_fixation',
            components=[fixation_cross],
        )
        r_fixation.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for r_fixation
        r_fixation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        r_fixation.tStart = globalClock.getTime(format='float')
        r_fixation.status = STARTED
        thisExp.addData('r_fixation.started', r_fixation.tStart)
        r_fixation.maxDuration = None
        # keep track of which components have finished
        r_fixationComponents = r_fixation.components
        for thisComponent in r_fixation.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "r_fixation" ---
        r_fixation.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisStimulus, 'status') and thisStimulus.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_cross* updates
            
            # if fixation_cross is starting this frame...
            if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_cross.frameNStart = frameN  # exact frame index
                fixation_cross.tStart = t  # local t and not account for scr refresh
                fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_cross.started')
                # update status
                fixation_cross.status = STARTED
                fixation_cross.setAutoDraw(True)
            
            # if fixation_cross is active this frame...
            if fixation_cross.status == STARTED:
                # update params
                pass
            
            # if fixation_cross is stopping this frame...
            if fixation_cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_cross.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_cross.tStop = t  # not accounting for scr refresh
                    fixation_cross.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation_cross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_cross.stopped')
                    # update status
                    fixation_cross.status = FINISHED
                    fixation_cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=r_fixation,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                r_fixation.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in r_fixation.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "r_fixation" ---
        for thisComponent in r_fixation.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for r_fixation
        r_fixation.tStop = globalClock.getTime(format='float')
        r_fixation.tStopRefresh = tThisFlipGlobal
        thisExp.addData('r_fixation.stopped', r_fixation.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if r_fixation.maxDurationReached:
            routineTimer.addTime(-r_fixation.maxDuration)
        elif r_fixation.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "r_video" ---
        # create an object to store info about Routine r_video
        r_video = data.Routine(
            name='r_video',
            components=[video],
        )
        r_video.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        video.setMovie(video_file)
        # store start times for r_video
        r_video.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        r_video.tStart = globalClock.getTime(format='float')
        r_video.status = STARTED
        thisExp.addData('r_video.started', r_video.tStart)
        r_video.maxDuration = None
        # keep track of which components have finished
        r_videoComponents = r_video.components
        for thisComponent in r_video.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "r_video" ---
        r_video.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 5.0:
            # if trial has changed, end Routine now
            if hasattr(thisStimulus, 'status') and thisStimulus.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *video* updates
            
            # if video is starting this frame...
            if video.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                video.frameNStart = frameN  # exact frame index
                video.tStart = t  # local t and not account for scr refresh
                video.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(video, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'video.started')
                # update status
                video.status = STARTED
                video.setAutoDraw(True)
                video.play()
            
            # if video is stopping this frame...
            if video.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > video.tStartRefresh + 5-frameTolerance or video.isFinished:
                    # keep track of stop time/frame for later
                    video.tStop = t  # not accounting for scr refresh
                    video.tStopRefresh = tThisFlipGlobal  # on global time
                    video.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'video.stopped')
                    # update status
                    video.status = FINISHED
                    video.setAutoDraw(False)
                    video.stop()
            if video.isFinished:  # force-end the Routine
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=r_video,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                r_video.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in r_video.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "r_video" ---
        for thisComponent in r_video.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for r_video
        r_video.tStop = globalClock.getTime(format='float')
        r_video.tStopRefresh = tThisFlipGlobal
        thisExp.addData('r_video.stopped', r_video.tStop)
        video.stop()  # ensure movie has stopped at end of Routine
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if r_video.maxDurationReached:
            routineTimer.addTime(-r_video.maxDuration)
        elif r_video.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        
        # --- Prepare to start Routine "r_SAM_1" ---
        # create an object to store info about Routine r_SAM_1
        r_SAM_1 = data.Routine(
            name='r_SAM_1',
            components=[question_sam_1_text, question_sam_1, rating_sam_1],
        )
        r_SAM_1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for rating_sam_1
        rating_sam_1.keys = []
        rating_sam_1.rt = []
        _rating_sam_1_allKeys = []
        # store start times for r_SAM_1
        r_SAM_1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        r_SAM_1.tStart = globalClock.getTime(format='float')
        r_SAM_1.status = STARTED
        thisExp.addData('r_SAM_1.started', r_SAM_1.tStart)
        r_SAM_1.maxDuration = None
        # keep track of which components have finished
        r_SAM_1Components = r_SAM_1.components
        for thisComponent in r_SAM_1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "r_SAM_1" ---
        r_SAM_1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisStimulus, 'status') and thisStimulus.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *question_sam_1_text* updates
            
            # if question_sam_1_text is starting this frame...
            if question_sam_1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                question_sam_1_text.frameNStart = frameN  # exact frame index
                question_sam_1_text.tStart = t  # local t and not account for scr refresh
                question_sam_1_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question_sam_1_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                question_sam_1_text.status = STARTED
                question_sam_1_text.setAutoDraw(True)
            
            # if question_sam_1_text is active this frame...
            if question_sam_1_text.status == STARTED:
                # update params
                pass
            
            # *question_sam_1* updates
            
            # if question_sam_1 is starting this frame...
            if question_sam_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                question_sam_1.frameNStart = frameN  # exact frame index
                question_sam_1.tStart = t  # local t and not account for scr refresh
                question_sam_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question_sam_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'question_sam_1.started')
                # update status
                question_sam_1.status = STARTED
                question_sam_1.setAutoDraw(True)
            
            # if question_sam_1 is active this frame...
            if question_sam_1.status == STARTED:
                # update params
                pass
            
            # *rating_sam_1* updates
            waitOnFlip = False
            
            # if rating_sam_1 is starting this frame...
            if rating_sam_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rating_sam_1.frameNStart = frameN  # exact frame index
                rating_sam_1.tStart = t  # local t and not account for scr refresh
                rating_sam_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rating_sam_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rating_sam_1.started')
                # update status
                rating_sam_1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(rating_sam_1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(rating_sam_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if rating_sam_1.status == STARTED and not waitOnFlip:
                theseKeys = rating_sam_1.getKeys(keyList=['1','2','3','4','5'], ignoreKeys=["escape"], waitRelease=False)
                _rating_sam_1_allKeys.extend(theseKeys)
                if len(_rating_sam_1_allKeys):
                    rating_sam_1.keys = _rating_sam_1_allKeys[-1].name  # just the last key pressed
                    rating_sam_1.rt = _rating_sam_1_allKeys[-1].rt
                    rating_sam_1.duration = _rating_sam_1_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=r_SAM_1,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                r_SAM_1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in r_SAM_1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "r_SAM_1" ---
        for thisComponent in r_SAM_1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for r_SAM_1
        r_SAM_1.tStop = globalClock.getTime(format='float')
        r_SAM_1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('r_SAM_1.stopped', r_SAM_1.tStop)
        # check responses
        if rating_sam_1.keys in ['', [], None]:  # No response was made
            rating_sam_1.keys = None
        stimuli.addData('rating_sam_1.keys',rating_sam_1.keys)
        if rating_sam_1.keys != None:  # we had a response
            stimuli.addData('rating_sam_1.rt', rating_sam_1.rt)
            stimuli.addData('rating_sam_1.duration', rating_sam_1.duration)
        # the Routine "r_SAM_1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "r_SAM_2" ---
        # create an object to store info about Routine r_SAM_2
        r_SAM_2 = data.Routine(
            name='r_SAM_2',
            components=[question_sam_2_text, question_sam_2, rating_sam_2],
        )
        r_SAM_2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for rating_sam_2
        rating_sam_2.keys = []
        rating_sam_2.rt = []
        _rating_sam_2_allKeys = []
        # store start times for r_SAM_2
        r_SAM_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        r_SAM_2.tStart = globalClock.getTime(format='float')
        r_SAM_2.status = STARTED
        thisExp.addData('r_SAM_2.started', r_SAM_2.tStart)
        r_SAM_2.maxDuration = None
        # keep track of which components have finished
        r_SAM_2Components = r_SAM_2.components
        for thisComponent in r_SAM_2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "r_SAM_2" ---
        r_SAM_2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisStimulus, 'status') and thisStimulus.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *question_sam_2_text* updates
            
            # if question_sam_2_text is starting this frame...
            if question_sam_2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                question_sam_2_text.frameNStart = frameN  # exact frame index
                question_sam_2_text.tStart = t  # local t and not account for scr refresh
                question_sam_2_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question_sam_2_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                question_sam_2_text.status = STARTED
                question_sam_2_text.setAutoDraw(True)
            
            # if question_sam_2_text is active this frame...
            if question_sam_2_text.status == STARTED:
                # update params
                pass
            
            # *question_sam_2* updates
            
            # if question_sam_2 is starting this frame...
            if question_sam_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                question_sam_2.frameNStart = frameN  # exact frame index
                question_sam_2.tStart = t  # local t and not account for scr refresh
                question_sam_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question_sam_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'question_sam_2.started')
                # update status
                question_sam_2.status = STARTED
                question_sam_2.setAutoDraw(True)
            
            # if question_sam_2 is active this frame...
            if question_sam_2.status == STARTED:
                # update params
                pass
            
            # *rating_sam_2* updates
            waitOnFlip = False
            
            # if rating_sam_2 is starting this frame...
            if rating_sam_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rating_sam_2.frameNStart = frameN  # exact frame index
                rating_sam_2.tStart = t  # local t and not account for scr refresh
                rating_sam_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rating_sam_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rating_sam_2.started')
                # update status
                rating_sam_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(rating_sam_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(rating_sam_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if rating_sam_2.status == STARTED and not waitOnFlip:
                theseKeys = rating_sam_2.getKeys(keyList=['1','2','3','4','5'], ignoreKeys=["escape"], waitRelease=False)
                _rating_sam_2_allKeys.extend(theseKeys)
                if len(_rating_sam_2_allKeys):
                    rating_sam_2.keys = _rating_sam_2_allKeys[-1].name  # just the last key pressed
                    rating_sam_2.rt = _rating_sam_2_allKeys[-1].rt
                    rating_sam_2.duration = _rating_sam_2_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=r_SAM_2,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                r_SAM_2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in r_SAM_2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "r_SAM_2" ---
        for thisComponent in r_SAM_2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for r_SAM_2
        r_SAM_2.tStop = globalClock.getTime(format='float')
        r_SAM_2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('r_SAM_2.stopped', r_SAM_2.tStop)
        # check responses
        if rating_sam_2.keys in ['', [], None]:  # No response was made
            rating_sam_2.keys = None
        stimuli.addData('rating_sam_2.keys',rating_sam_2.keys)
        if rating_sam_2.keys != None:  # we had a response
            stimuli.addData('rating_sam_2.rt', rating_sam_2.rt)
            stimuli.addData('rating_sam_2.duration', rating_sam_2.duration)
        # the Routine "r_SAM_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "r_SAM_3" ---
        # create an object to store info about Routine r_SAM_3
        r_SAM_3 = data.Routine(
            name='r_SAM_3',
            components=[question_sam_3_text, question_sam_3, rating_sam_3],
        )
        r_SAM_3.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for rating_sam_3
        rating_sam_3.keys = []
        rating_sam_3.rt = []
        _rating_sam_3_allKeys = []
        # store start times for r_SAM_3
        r_SAM_3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        r_SAM_3.tStart = globalClock.getTime(format='float')
        r_SAM_3.status = STARTED
        thisExp.addData('r_SAM_3.started', r_SAM_3.tStart)
        r_SAM_3.maxDuration = None
        # keep track of which components have finished
        r_SAM_3Components = r_SAM_3.components
        for thisComponent in r_SAM_3.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "r_SAM_3" ---
        r_SAM_3.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisStimulus, 'status') and thisStimulus.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *question_sam_3_text* updates
            
            # if question_sam_3_text is starting this frame...
            if question_sam_3_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                question_sam_3_text.frameNStart = frameN  # exact frame index
                question_sam_3_text.tStart = t  # local t and not account for scr refresh
                question_sam_3_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question_sam_3_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                question_sam_3_text.status = STARTED
                question_sam_3_text.setAutoDraw(True)
            
            # if question_sam_3_text is active this frame...
            if question_sam_3_text.status == STARTED:
                # update params
                pass
            
            # *question_sam_3* updates
            
            # if question_sam_3 is starting this frame...
            if question_sam_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                question_sam_3.frameNStart = frameN  # exact frame index
                question_sam_3.tStart = t  # local t and not account for scr refresh
                question_sam_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question_sam_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'question_sam_3.started')
                # update status
                question_sam_3.status = STARTED
                question_sam_3.setAutoDraw(True)
            
            # if question_sam_3 is active this frame...
            if question_sam_3.status == STARTED:
                # update params
                pass
            
            # *rating_sam_3* updates
            waitOnFlip = False
            
            # if rating_sam_3 is starting this frame...
            if rating_sam_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rating_sam_3.frameNStart = frameN  # exact frame index
                rating_sam_3.tStart = t  # local t and not account for scr refresh
                rating_sam_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rating_sam_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rating_sam_3.started')
                # update status
                rating_sam_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(rating_sam_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(rating_sam_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if rating_sam_3.status == STARTED and not waitOnFlip:
                theseKeys = rating_sam_3.getKeys(keyList=['1','2','3','4','5'], ignoreKeys=["escape"], waitRelease=False)
                _rating_sam_3_allKeys.extend(theseKeys)
                if len(_rating_sam_3_allKeys):
                    rating_sam_3.keys = _rating_sam_3_allKeys[-1].name  # just the last key pressed
                    rating_sam_3.rt = _rating_sam_3_allKeys[-1].rt
                    rating_sam_3.duration = _rating_sam_3_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=r_SAM_3,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                r_SAM_3.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in r_SAM_3.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "r_SAM_3" ---
        for thisComponent in r_SAM_3.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for r_SAM_3
        r_SAM_3.tStop = globalClock.getTime(format='float')
        r_SAM_3.tStopRefresh = tThisFlipGlobal
        thisExp.addData('r_SAM_3.stopped', r_SAM_3.tStop)
        # check responses
        if rating_sam_3.keys in ['', [], None]:  # No response was made
            rating_sam_3.keys = None
        stimuli.addData('rating_sam_3.keys',rating_sam_3.keys)
        if rating_sam_3.keys != None:  # we had a response
            stimuli.addData('rating_sam_3.rt', rating_sam_3.rt)
            stimuli.addData('rating_sam_3.duration', rating_sam_3.duration)
        # the Routine "r_SAM_3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "r_focus_questionnaire" ---
        # create an object to store info about Routine r_focus_questionnaire
        r_focus_questionnaire = data.Routine(
            name='r_focus_questionnaire',
            components=[focus_text, focus_slider],
        )
        r_focus_questionnaire.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        focus_slider.reset()
        # store start times for r_focus_questionnaire
        r_focus_questionnaire.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        r_focus_questionnaire.tStart = globalClock.getTime(format='float')
        r_focus_questionnaire.status = STARTED
        thisExp.addData('r_focus_questionnaire.started', r_focus_questionnaire.tStart)
        r_focus_questionnaire.maxDuration = None
        # keep track of which components have finished
        r_focus_questionnaireComponents = r_focus_questionnaire.components
        for thisComponent in r_focus_questionnaire.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "r_focus_questionnaire" ---
        r_focus_questionnaire.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisStimulus, 'status') and thisStimulus.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *focus_text* updates
            
            # if focus_text is starting this frame...
            if focus_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                focus_text.frameNStart = frameN  # exact frame index
                focus_text.tStart = t  # local t and not account for scr refresh
                focus_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(focus_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                focus_text.status = STARTED
                focus_text.setAutoDraw(True)
            
            # if focus_text is active this frame...
            if focus_text.status == STARTED:
                # update params
                pass
            
            # *focus_slider* updates
            
            # if focus_slider is starting this frame...
            if focus_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                focus_slider.frameNStart = frameN  # exact frame index
                focus_slider.tStart = t  # local t and not account for scr refresh
                focus_slider.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(focus_slider, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'focus_slider.started')
                # update status
                focus_slider.status = STARTED
                focus_slider.setAutoDraw(True)
            
            # if focus_slider is active this frame...
            if focus_slider.status == STARTED:
                # update params
                pass
            
            # Check focus_slider for response to end Routine
            if focus_slider.getRating() is not None and focus_slider.status == STARTED:
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=r_focus_questionnaire,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                r_focus_questionnaire.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in r_focus_questionnaire.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "r_focus_questionnaire" ---
        for thisComponent in r_focus_questionnaire.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for r_focus_questionnaire
        r_focus_questionnaire.tStop = globalClock.getTime(format='float')
        r_focus_questionnaire.tStopRefresh = tThisFlipGlobal
        thisExp.addData('r_focus_questionnaire.stopped', r_focus_questionnaire.tStop)
        stimuli.addData('focus_slider.response', focus_slider.getRating())
        stimuli.addData('focus_slider.rt', focus_slider.getRT())
        # the Routine "r_focus_questionnaire" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisStimulus as finished
        if hasattr(thisStimulus, 'status'):
            thisStimulus.status = FINISHED
        # if awaiting a pause, pause now
        if stimuli.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            stimuli.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'stimuli'
    stimuli.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "r_final_questionnaire" ---
    # create an object to store info about Routine r_final_questionnaire
    r_final_questionnaire = data.Routine(
        name='r_final_questionnaire',
        components=[opinion_text, opinion_slider],
    )
    r_final_questionnaire.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    opinion_slider.reset()
    # store start times for r_final_questionnaire
    r_final_questionnaire.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    r_final_questionnaire.tStart = globalClock.getTime(format='float')
    r_final_questionnaire.status = STARTED
    thisExp.addData('r_final_questionnaire.started', r_final_questionnaire.tStart)
    r_final_questionnaire.maxDuration = None
    # keep track of which components have finished
    r_final_questionnaireComponents = r_final_questionnaire.components
    for thisComponent in r_final_questionnaire.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "r_final_questionnaire" ---
    r_final_questionnaire.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *opinion_text* updates
        
        # if opinion_text is starting this frame...
        if opinion_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            opinion_text.frameNStart = frameN  # exact frame index
            opinion_text.tStart = t  # local t and not account for scr refresh
            opinion_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(opinion_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            opinion_text.status = STARTED
            opinion_text.setAutoDraw(True)
        
        # if opinion_text is active this frame...
        if opinion_text.status == STARTED:
            # update params
            pass
        
        # *opinion_slider* updates
        
        # if opinion_slider is starting this frame...
        if opinion_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            opinion_slider.frameNStart = frameN  # exact frame index
            opinion_slider.tStart = t  # local t and not account for scr refresh
            opinion_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(opinion_slider, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'opinion_slider.started')
            # update status
            opinion_slider.status = STARTED
            opinion_slider.setAutoDraw(True)
        
        # if opinion_slider is active this frame...
        if opinion_slider.status == STARTED:
            # update params
            pass
        
        # Check opinion_slider for response to end Routine
        if opinion_slider.getRating() is not None and opinion_slider.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=r_final_questionnaire,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            r_final_questionnaire.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in r_final_questionnaire.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "r_final_questionnaire" ---
    for thisComponent in r_final_questionnaire.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for r_final_questionnaire
    r_final_questionnaire.tStop = globalClock.getTime(format='float')
    r_final_questionnaire.tStopRefresh = tThisFlipGlobal
    thisExp.addData('r_final_questionnaire.stopped', r_final_questionnaire.tStop)
    thisExp.addData('opinion_slider.response', opinion_slider.getRating())
    thisExp.addData('opinion_slider.rt', opinion_slider.getRT())
    thisExp.nextEntry()
    # the Routine "r_final_questionnaire" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    # Run 'End Experiment' code from load_design
    thisExp.addData('expEndTime', time.time())
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
