#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2025.1.1),
    on Wed Nov  5 12:10:37 2025
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
        originPath='/Users/francesco/Documents/dev/02455-Experiment-In-Cognitive-Science/manipulation-of-belief.py',
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
            winType='pyglet', allowGUI=False, allowStencil=False,
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
    if deviceManager.getDevice('skip_video') is None:
        # initialise skip_video
        skip_video = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='skip_video',
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
    if deviceManager.getDevice('questionnaire_done') is None:
        # initialise questionnaire_done
        questionnaire_done = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='questionnaire_done',
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
    
    # --- Initialize components for Routine "instructions" ---
    text_norm = visual.TextStim(win=win, name='text_norm',
        text='Any text\n\nincluding line breaks\n\nThis text component is white, so change the colour if you have a white background. It does not save the onset and offset time, but has been left justified with a wrap width of 1.8 norm units.\n\nPress the spacebar to continue',
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
    text_norm.alignText= 'left'
    
    # --- Initialize components for Routine "preparation" ---
    # Run 'Begin Experiment' code from load_design
    import csv
    
    stimuli_design = []
    with open('variables/subjects_design.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stimuli_design.append(row)
    
    subj_num = int(expInfo['participant'])
    selected_order = stimuli_design[subj_num]
    print(f"Subject {subj_num} - selected order: {selected_order}")
    video_nature_type = visual.TextStim(win=win, name='video_nature_type',
        text='',
        font='Arial',
        units='norm', pos=(0, 0), draggable=False, height=0.1, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "video" ---
    video_stimuli = visual.MovieStim(
        win, name='video_stimuli',
        filename=None, movieLib='ffpyplayer',
        loop=False, volume=1.0, noAudio=False,
        pos=(0, 0), size=None, units=win.units,
        ori=0.0, anchor='center',opacity=None, contrast=1.0,
        depth=0
    )
    fixation_cross = visual.ShapeStim(
        win=win, name='fixation_cross', vertices='cross',
        size=(30,30),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor=[-0.1765, -0.1765, -0.1765],
        opacity=None, depth=-1.0, interpolate=True)
    skip_video = keyboard.Keyboard(deviceName='skip_video')
    
    # --- Initialize components for Routine "SAM_1" ---
    question_sam_1 = visual.ImageStim(
        win=win,
        name='question_sam_1', 
        image='stimuli/sam-1.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    rating_sam_1 = keyboard.Keyboard(deviceName='rating_sam_1')
    
    # --- Initialize components for Routine "SAM_2" ---
    question_sam_2 = visual.ImageStim(
        win=win,
        name='question_sam_2', 
        image='stimuli/sam-2.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    rating_sam_2 = keyboard.Keyboard(deviceName='rating_sam_2')
    
    # --- Initialize components for Routine "SAM_3" ---
    question_sam_3 = visual.ImageStim(
        win=win,
        name='question_sam_3', 
        image='stimuli/sam-3.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    rating_sam_3 = keyboard.Keyboard(deviceName='rating_sam_3')
    
    # --- Initialize components for Routine "questionnaire" ---
    win.allowStencil = True
    questionnaire_form = visual.Form(win=win, name='questionnaire_form',
        items='variables/questionnaire_form.xlsx',
        textHeight=0.01,
        font='Arial',
        randomize=False,
        style='dark',
        fillColor=None, borderColor=None, itemColor='white', 
        responseColor='white', markerColor='red', colorSpace='rgb', 
        size=None,
        pos=(0, 0),
        itemPadding=0.02,
        depth=0
    )
    questionnaire_done = keyboard.Keyboard(deviceName='questionnaire_done')
    
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
    
    # --- Prepare to start Routine "instructions" ---
    # create an object to store info about Routine instructions
    instructions = data.Routine(
        name='instructions',
        components=[text_norm, key_instruct],
    )
    instructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_instruct
    key_instruct.keys = []
    key_instruct.rt = []
    _key_instruct_allKeys = []
    # store start times for instructions
    instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructions.tStart = globalClock.getTime(format='float')
    instructions.status = STARTED
    thisExp.addData('instructions.started', instructions.tStart)
    instructions.maxDuration = None
    # keep track of which components have finished
    instructionsComponents = instructions.components
    for thisComponent in instructions.components:
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
    
    # --- Run Routine "instructions" ---
    instructions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_norm* updates
        
        # if text_norm is starting this frame...
        if text_norm.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_norm.frameNStart = frameN  # exact frame index
            text_norm.tStart = t  # local t and not account for scr refresh
            text_norm.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_norm, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_norm.status = STARTED
            text_norm.setAutoDraw(True)
        
        # if text_norm is active this frame...
        if text_norm.status == STARTED:
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
                currentRoutine=instructions,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instructions.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions" ---
    for thisComponent in instructions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructions
    instructions.tStop = globalClock.getTime(format='float')
    instructions.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instructions.stopped', instructions.tStop)
    # check responses
    if key_instruct.keys in ['', [], None]:  # No response was made
        key_instruct.keys = None
    thisExp.addData('key_instruct.keys',key_instruct.keys)
    if key_instruct.keys != None:  # we had a response
        thisExp.addData('key_instruct.rt', key_instruct.rt)
        thisExp.addData('key_instruct.duration', key_instruct.duration)
    thisExp.nextEntry()
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
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
        
        # --- Prepare to start Routine "preparation" ---
        # create an object to store info about Routine preparation
        preparation = data.Routine(
            name='preparation',
            components=[video_nature_type],
        )
        preparation.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from load_design
        video_file = 'stimuli/' + selected_order[f'video{video_index}']
        label_text = selected_order[f'label{video_index}']
        # store start times for preparation
        preparation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        preparation.tStart = globalClock.getTime(format='float')
        preparation.status = STARTED
        thisExp.addData('preparation.started', preparation.tStart)
        preparation.maxDuration = None
        # keep track of which components have finished
        preparationComponents = preparation.components
        for thisComponent in preparation.components:
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
        
        # --- Run Routine "preparation" ---
        preparation.forceEnded = routineForceEnded = not continueRoutine
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
            
            # *video_nature_type* updates
            
            # if video_nature_type is starting this frame...
            if video_nature_type.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                video_nature_type.frameNStart = frameN  # exact frame index
                video_nature_type.tStart = t  # local t and not account for scr refresh
                video_nature_type.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(video_nature_type, 'tStartRefresh')  # time at next scr refresh
                # update status
                video_nature_type.status = STARTED
                video_nature_type.setAutoDraw(True)
            
            # if video_nature_type is active this frame...
            if video_nature_type.status == STARTED:
                # update params
                video_nature_type.setText("The next video is going to be " + str(label_text) + "\n" + str(5-int(t)), log=False)
            
            # if video_nature_type is stopping this frame...
            if video_nature_type.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > video_nature_type.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    video_nature_type.tStop = t  # not accounting for scr refresh
                    video_nature_type.tStopRefresh = tThisFlipGlobal  # on global time
                    video_nature_type.frameNStop = frameN  # exact frame index
                    # update status
                    video_nature_type.status = FINISHED
                    video_nature_type.setAutoDraw(False)
            
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
                    currentRoutine=preparation,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                preparation.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in preparation.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "preparation" ---
        for thisComponent in preparation.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for preparation
        preparation.tStop = globalClock.getTime(format='float')
        preparation.tStopRefresh = tThisFlipGlobal
        thisExp.addData('preparation.stopped', preparation.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if preparation.maxDurationReached:
            routineTimer.addTime(-preparation.maxDuration)
        elif preparation.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        
        # --- Prepare to start Routine "video" ---
        # create an object to store info about Routine video
        video = data.Routine(
            name='video',
            components=[video_stimuli, fixation_cross, skip_video],
        )
        video.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        video_stimuli.setMovie(video_file)
        # create starting attributes for skip_video
        skip_video.keys = []
        skip_video.rt = []
        _skip_video_allKeys = []
        # store start times for video
        video.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        video.tStart = globalClock.getTime(format='float')
        video.status = STARTED
        thisExp.addData('video.started', video.tStart)
        video.maxDuration = None
        # keep track of which components have finished
        videoComponents = video.components
        for thisComponent in video.components:
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
        
        # --- Run Routine "video" ---
        video.forceEnded = routineForceEnded = not continueRoutine
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
            
            # *video_stimuli* updates
            
            # if video_stimuli is starting this frame...
            if video_stimuli.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                video_stimuli.frameNStart = frameN  # exact frame index
                video_stimuli.tStart = t  # local t and not account for scr refresh
                video_stimuli.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(video_stimuli, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'video_stimuli.started')
                # update status
                video_stimuli.status = STARTED
                video_stimuli.setAutoDraw(True)
                video_stimuli.play()
            
            # if video_stimuli is stopping this frame...
            if video_stimuli.status == STARTED:
                if bool(False) or video_stimuli.isFinished:
                    # keep track of stop time/frame for later
                    video_stimuli.tStop = t  # not accounting for scr refresh
                    video_stimuli.tStopRefresh = tThisFlipGlobal  # on global time
                    video_stimuli.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'video_stimuli.stopped')
                    # update status
                    video_stimuli.status = FINISHED
                    video_stimuli.setAutoDraw(False)
                    video_stimuli.stop()
            if video_stimuli.isFinished:  # force-end the Routine
                continueRoutine = False
            
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
            
            # *skip_video* updates
            waitOnFlip = False
            
            # if skip_video is starting this frame...
            if skip_video.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                skip_video.frameNStart = frameN  # exact frame index
                skip_video.tStart = t  # local t and not account for scr refresh
                skip_video.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(skip_video, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'skip_video.started')
                # update status
                skip_video.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(skip_video.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(skip_video.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if skip_video.status == STARTED and not waitOnFlip:
                theseKeys = skip_video.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _skip_video_allKeys.extend(theseKeys)
                if len(_skip_video_allKeys):
                    skip_video.keys = _skip_video_allKeys[-1].name  # just the last key pressed
                    skip_video.rt = _skip_video_allKeys[-1].rt
                    skip_video.duration = _skip_video_allKeys[-1].duration
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
                    currentRoutine=video,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                video.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in video.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "video" ---
        for thisComponent in video.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for video
        video.tStop = globalClock.getTime(format='float')
        video.tStopRefresh = tThisFlipGlobal
        thisExp.addData('video.stopped', video.tStop)
        video_stimuli.stop()  # ensure movie has stopped at end of Routine
        # check responses
        if skip_video.keys in ['', [], None]:  # No response was made
            skip_video.keys = None
        stimuli.addData('skip_video.keys',skip_video.keys)
        if skip_video.keys != None:  # we had a response
            stimuli.addData('skip_video.rt', skip_video.rt)
            stimuli.addData('skip_video.duration', skip_video.duration)
        # the Routine "video" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "SAM_1" ---
        # create an object to store info about Routine SAM_1
        SAM_1 = data.Routine(
            name='SAM_1',
            components=[question_sam_1, rating_sam_1],
        )
        SAM_1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for rating_sam_1
        rating_sam_1.keys = []
        rating_sam_1.rt = []
        _rating_sam_1_allKeys = []
        # store start times for SAM_1
        SAM_1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        SAM_1.tStart = globalClock.getTime(format='float')
        SAM_1.status = STARTED
        thisExp.addData('SAM_1.started', SAM_1.tStart)
        SAM_1.maxDuration = None
        # keep track of which components have finished
        SAM_1Components = SAM_1.components
        for thisComponent in SAM_1.components:
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
        
        # --- Run Routine "SAM_1" ---
        SAM_1.forceEnded = routineForceEnded = not continueRoutine
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
                theseKeys = rating_sam_1.getKeys(keyList=['1','2','3','4','5','6','7','8','9'], ignoreKeys=["escape"], waitRelease=False)
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
                    currentRoutine=SAM_1,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                SAM_1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in SAM_1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "SAM_1" ---
        for thisComponent in SAM_1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for SAM_1
        SAM_1.tStop = globalClock.getTime(format='float')
        SAM_1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('SAM_1.stopped', SAM_1.tStop)
        # check responses
        if rating_sam_1.keys in ['', [], None]:  # No response was made
            rating_sam_1.keys = None
        stimuli.addData('rating_sam_1.keys',rating_sam_1.keys)
        if rating_sam_1.keys != None:  # we had a response
            stimuli.addData('rating_sam_1.rt', rating_sam_1.rt)
            stimuli.addData('rating_sam_1.duration', rating_sam_1.duration)
        # the Routine "SAM_1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "SAM_2" ---
        # create an object to store info about Routine SAM_2
        SAM_2 = data.Routine(
            name='SAM_2',
            components=[question_sam_2, rating_sam_2],
        )
        SAM_2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for rating_sam_2
        rating_sam_2.keys = []
        rating_sam_2.rt = []
        _rating_sam_2_allKeys = []
        # store start times for SAM_2
        SAM_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        SAM_2.tStart = globalClock.getTime(format='float')
        SAM_2.status = STARTED
        thisExp.addData('SAM_2.started', SAM_2.tStart)
        SAM_2.maxDuration = None
        # keep track of which components have finished
        SAM_2Components = SAM_2.components
        for thisComponent in SAM_2.components:
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
        
        # --- Run Routine "SAM_2" ---
        SAM_2.forceEnded = routineForceEnded = not continueRoutine
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
                theseKeys = rating_sam_2.getKeys(keyList=['1','2','3','4','5','6','7','8','9'], ignoreKeys=["escape"], waitRelease=False)
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
                    currentRoutine=SAM_2,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                SAM_2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in SAM_2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "SAM_2" ---
        for thisComponent in SAM_2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for SAM_2
        SAM_2.tStop = globalClock.getTime(format='float')
        SAM_2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('SAM_2.stopped', SAM_2.tStop)
        # check responses
        if rating_sam_2.keys in ['', [], None]:  # No response was made
            rating_sam_2.keys = None
        stimuli.addData('rating_sam_2.keys',rating_sam_2.keys)
        if rating_sam_2.keys != None:  # we had a response
            stimuli.addData('rating_sam_2.rt', rating_sam_2.rt)
            stimuli.addData('rating_sam_2.duration', rating_sam_2.duration)
        # the Routine "SAM_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "SAM_3" ---
        # create an object to store info about Routine SAM_3
        SAM_3 = data.Routine(
            name='SAM_3',
            components=[question_sam_3, rating_sam_3],
        )
        SAM_3.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for rating_sam_3
        rating_sam_3.keys = []
        rating_sam_3.rt = []
        _rating_sam_3_allKeys = []
        # store start times for SAM_3
        SAM_3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        SAM_3.tStart = globalClock.getTime(format='float')
        SAM_3.status = STARTED
        thisExp.addData('SAM_3.started', SAM_3.tStart)
        SAM_3.maxDuration = None
        # keep track of which components have finished
        SAM_3Components = SAM_3.components
        for thisComponent in SAM_3.components:
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
        
        # --- Run Routine "SAM_3" ---
        SAM_3.forceEnded = routineForceEnded = not continueRoutine
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
                theseKeys = rating_sam_3.getKeys(keyList=['1','2','3','4','5','6','7','8','9'], ignoreKeys=["escape"], waitRelease=False)
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
                    currentRoutine=SAM_3,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                SAM_3.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in SAM_3.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "SAM_3" ---
        for thisComponent in SAM_3.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for SAM_3
        SAM_3.tStop = globalClock.getTime(format='float')
        SAM_3.tStopRefresh = tThisFlipGlobal
        thisExp.addData('SAM_3.stopped', SAM_3.tStop)
        # check responses
        if rating_sam_3.keys in ['', [], None]:  # No response was made
            rating_sam_3.keys = None
        stimuli.addData('rating_sam_3.keys',rating_sam_3.keys)
        if rating_sam_3.keys != None:  # we had a response
            stimuli.addData('rating_sam_3.rt', rating_sam_3.rt)
            stimuli.addData('rating_sam_3.duration', rating_sam_3.duration)
        # the Routine "SAM_3" was not non-slip safe, so reset the non-slip timer
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
    
    # --- Prepare to start Routine "questionnaire" ---
    # create an object to store info about Routine questionnaire
    questionnaire = data.Routine(
        name='questionnaire',
        components=[questionnaire_form, questionnaire_done],
    )
    questionnaire.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for questionnaire_done
    questionnaire_done.keys = []
    questionnaire_done.rt = []
    _questionnaire_done_allKeys = []
    # store start times for questionnaire
    questionnaire.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    questionnaire.tStart = globalClock.getTime(format='float')
    questionnaire.status = STARTED
    thisExp.addData('questionnaire.started', questionnaire.tStart)
    questionnaire.maxDuration = None
    # keep track of which components have finished
    questionnaireComponents = questionnaire.components
    for thisComponent in questionnaire.components:
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
    
    # --- Run Routine "questionnaire" ---
    questionnaire.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *questionnaire_form* updates
        
        # if questionnaire_form is starting this frame...
        if questionnaire_form.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            questionnaire_form.frameNStart = frameN  # exact frame index
            questionnaire_form.tStart = t  # local t and not account for scr refresh
            questionnaire_form.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(questionnaire_form, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'questionnaire_form.started')
            # update status
            questionnaire_form.status = STARTED
            questionnaire_form.setAutoDraw(True)
        
        # if questionnaire_form is active this frame...
        if questionnaire_form.status == STARTED:
            # update params
            pass
        
        # *questionnaire_done* updates
        waitOnFlip = False
        
        # if questionnaire_done is starting this frame...
        if questionnaire_done.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            questionnaire_done.frameNStart = frameN  # exact frame index
            questionnaire_done.tStart = t  # local t and not account for scr refresh
            questionnaire_done.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(questionnaire_done, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'questionnaire_done.started')
            # update status
            questionnaire_done.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(questionnaire_done.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(questionnaire_done.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if questionnaire_done.status == STARTED and not waitOnFlip:
            theseKeys = questionnaire_done.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _questionnaire_done_allKeys.extend(theseKeys)
            if len(_questionnaire_done_allKeys):
                questionnaire_done.keys = _questionnaire_done_allKeys[-1].name  # just the last key pressed
                questionnaire_done.rt = _questionnaire_done_allKeys[-1].rt
                questionnaire_done.duration = _questionnaire_done_allKeys[-1].duration
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
                currentRoutine=questionnaire,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            questionnaire.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in questionnaire.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "questionnaire" ---
    for thisComponent in questionnaire.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for questionnaire
    questionnaire.tStop = globalClock.getTime(format='float')
    questionnaire.tStopRefresh = tThisFlipGlobal
    thisExp.addData('questionnaire.stopped', questionnaire.tStop)
    questionnaire_form.addDataToExp(thisExp, 'rows')
    questionnaire_form.autodraw = False
    # check responses
    if questionnaire_done.keys in ['', [], None]:  # No response was made
        questionnaire_done.keys = None
    thisExp.addData('questionnaire_done.keys',questionnaire_done.keys)
    if questionnaire_done.keys != None:  # we had a response
        thisExp.addData('questionnaire_done.rt', questionnaire_done.rt)
        thisExp.addData('questionnaire_done.duration', questionnaire_done.duration)
    thisExp.nextEntry()
    # the Routine "questionnaire" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
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
