/******************************* 
 * Manipulation-Of-Belief *
 *******************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2025.1.1.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'manipulation-of-belief';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};
let PILOTING = util.getUrlParameters().has('__pilotToken');

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);





flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'variables/subjects_design.csv', 'path': 'variables/subjects_design.csv'},
    {'name': 'stimuli/sam-1.png', 'path': 'stimuli/sam-1.png'},
    {'name': 'stimuli/sam-2.png', 'path': 'stimuli/sam-2.png'},
    {'name': 'stimuli/sam-3.png', 'path': 'stimuli/sam-3.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2025.1.1';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var videoClock;
var video1Clock;
var video1;
var text;
var SAM_1Clock;
var question_sam_1;
var rating_sam_1;
var SAM_2Clock;
var question_sam_2;
var rating_sam_2;
var SAM_3Clock;
var question_sam_3;
var rating_sam_3;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "video"
  videoClock = new util.Clock();
  // Run 'Begin Experiment' code from load_design
  /* Syntax Error: Fix Python code */
  video1Clock = new util.Clock();
  video1 = new visual.MovieStim({
    win: psychoJS.window,
    movie: null,
    name: 'video1',
    units: psychoJS.window.units,
    pos: [0, 0],
    anchor: 'center',
    size: [0.5, 0.5],
    ori: 0.0,
    opacity: null,
    loop: false,
    noAudio: false,
    depth: -1
  })
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "SAM_1"
  SAM_1Clock = new util.Clock();
  question_sam_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'question_sam_1', units : undefined, 
    image : 'stimuli/sam-1.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  rating_sam_1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SAM_2"
  SAM_2Clock = new util.Clock();
  question_sam_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'question_sam_2', units : undefined, 
    image : 'stimuli/sam-2.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  rating_sam_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SAM_3"
  SAM_3Clock = new util.Clock();
  question_sam_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'question_sam_3', units : undefined, 
    image : 'stimuli/sam-3.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  rating_sam_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 4, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'variables/subjects_design.csv',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(videoRoutineBegin(snapshot));
      trialsLoopScheduler.add(videoRoutineEachFrame());
      trialsLoopScheduler.add(videoRoutineEnd(snapshot));
      trialsLoopScheduler.add(SAM_1RoutineBegin(snapshot));
      trialsLoopScheduler.add(SAM_1RoutineEachFrame());
      trialsLoopScheduler.add(SAM_1RoutineEnd(snapshot));
      trialsLoopScheduler.add(SAM_2RoutineBegin(snapshot));
      trialsLoopScheduler.add(SAM_2RoutineEachFrame());
      trialsLoopScheduler.add(SAM_2RoutineEnd(snapshot));
      trialsLoopScheduler.add(SAM_3RoutineBegin(snapshot));
      trialsLoopScheduler.add(SAM_3RoutineEachFrame());
      trialsLoopScheduler.add(SAM_3RoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var t;
var frameN;
var continueRoutine;
var routineForceEnded;
var videoMaxDurationReached;
var videoMaxDuration;
var videoComponents;
function videoRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'video' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    videoClock.reset(routineTimer.getTime());
    routineTimer.add(3.000000);
    videoMaxDurationReached = false;
    // update component parameters for each repeat
    video1.setMovie(videoFileName);
    text.setText(label);
    psychoJS.experiment.addData('video.started', globalClock.getTime());
    videoMaxDuration = null
    // keep track of which components have finished
    videoComponents = [];
    videoComponents.push(video1);
    videoComponents.push(text);
    
    for (const thisComponent of videoComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function videoRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'video' ---
    // get current time
    t = videoClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *video1* updates
    if (t >= 0.0 && video1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      video1.tStart = t;  // (not accounting for frame time here)
      video1.frameNStart = frameN;  // exact frame index
      
      video1.setAutoDraw(true);
      video1.play();
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (video1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      video1.tStop = t;  // not accounting for scr refresh
      video1.frameNStop = frameN;  // exact frame index
      // update status
      video1.status = PsychoJS.Status.FINISHED;
      video1.setAutoDraw(false);
    }
    
    if (video1.status === PsychoJS.Status.FINISHED) {  // force-end the Routine
        continueRoutine = false;
    }
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    
    // if text is active this frame...
    if (text.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text.tStop = t;  // not accounting for scr refresh
      text.frameNStop = frameN;  // exact frame index
      // update status
      text.status = PsychoJS.Status.FINISHED;
      text.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of videoComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function videoRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'video' ---
    for (const thisComponent of videoComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('video.stopped', globalClock.getTime());
    video1.stop();  // ensure movie has stopped at end of Routine
    if (routineForceEnded) {
        routineTimer.reset();} else if (videoMaxDurationReached) {
        videoClock.add(videoMaxDuration);
    } else {
        videoClock.add(3.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var SAM_1MaxDurationReached;
var _rating_sam_1_allKeys;
var SAM_1MaxDuration;
var SAM_1Components;
function SAM_1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SAM_1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    SAM_1Clock.reset();
    routineTimer.reset();
    SAM_1MaxDurationReached = false;
    // update component parameters for each repeat
    rating_sam_1.keys = undefined;
    rating_sam_1.rt = undefined;
    _rating_sam_1_allKeys = [];
    psychoJS.experiment.addData('SAM_1.started', globalClock.getTime());
    SAM_1MaxDuration = null
    // keep track of which components have finished
    SAM_1Components = [];
    SAM_1Components.push(question_sam_1);
    SAM_1Components.push(rating_sam_1);
    
    for (const thisComponent of SAM_1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function SAM_1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SAM_1' ---
    // get current time
    t = SAM_1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *question_sam_1* updates
    if (t >= 0.0 && question_sam_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      question_sam_1.tStart = t;  // (not accounting for frame time here)
      question_sam_1.frameNStart = frameN;  // exact frame index
      
      question_sam_1.setAutoDraw(true);
    }
    
    
    // if question_sam_1 is active this frame...
    if (question_sam_1.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *rating_sam_1* updates
    if (t >= 0.0 && rating_sam_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rating_sam_1.tStart = t;  // (not accounting for frame time here)
      rating_sam_1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { rating_sam_1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { rating_sam_1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { rating_sam_1.clearEvents(); });
    }
    
    // if rating_sam_1 is active this frame...
    if (rating_sam_1.status === PsychoJS.Status.STARTED) {
      let theseKeys = rating_sam_1.getKeys({keyList: ['1','2','3','4','5','6','7','8','9'], waitRelease: false});
      _rating_sam_1_allKeys = _rating_sam_1_allKeys.concat(theseKeys);
      if (_rating_sam_1_allKeys.length > 0) {
        rating_sam_1.keys = _rating_sam_1_allKeys[_rating_sam_1_allKeys.length - 1].name;  // just the last key pressed
        rating_sam_1.rt = _rating_sam_1_allKeys[_rating_sam_1_allKeys.length - 1].rt;
        rating_sam_1.duration = _rating_sam_1_allKeys[_rating_sam_1_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of SAM_1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SAM_1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SAM_1' ---
    for (const thisComponent of SAM_1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('SAM_1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(rating_sam_1.corr, level);
    }
    psychoJS.experiment.addData('rating_sam_1.keys', rating_sam_1.keys);
    if (typeof rating_sam_1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('rating_sam_1.rt', rating_sam_1.rt);
        psychoJS.experiment.addData('rating_sam_1.duration', rating_sam_1.duration);
        routineTimer.reset();
        }
    
    rating_sam_1.stop();
    // the Routine "SAM_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var SAM_2MaxDurationReached;
var _rating_sam_2_allKeys;
var SAM_2MaxDuration;
var SAM_2Components;
function SAM_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SAM_2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    SAM_2Clock.reset();
    routineTimer.reset();
    SAM_2MaxDurationReached = false;
    // update component parameters for each repeat
    rating_sam_2.keys = undefined;
    rating_sam_2.rt = undefined;
    _rating_sam_2_allKeys = [];
    psychoJS.experiment.addData('SAM_2.started', globalClock.getTime());
    SAM_2MaxDuration = null
    // keep track of which components have finished
    SAM_2Components = [];
    SAM_2Components.push(question_sam_2);
    SAM_2Components.push(rating_sam_2);
    
    for (const thisComponent of SAM_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function SAM_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SAM_2' ---
    // get current time
    t = SAM_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *question_sam_2* updates
    if (t >= 0.0 && question_sam_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      question_sam_2.tStart = t;  // (not accounting for frame time here)
      question_sam_2.frameNStart = frameN;  // exact frame index
      
      question_sam_2.setAutoDraw(true);
    }
    
    
    // if question_sam_2 is active this frame...
    if (question_sam_2.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *rating_sam_2* updates
    if (t >= 0.0 && rating_sam_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rating_sam_2.tStart = t;  // (not accounting for frame time here)
      rating_sam_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { rating_sam_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { rating_sam_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { rating_sam_2.clearEvents(); });
    }
    
    // if rating_sam_2 is active this frame...
    if (rating_sam_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = rating_sam_2.getKeys({keyList: ['1','2','3','4','5','6','7','8','9'], waitRelease: false});
      _rating_sam_2_allKeys = _rating_sam_2_allKeys.concat(theseKeys);
      if (_rating_sam_2_allKeys.length > 0) {
        rating_sam_2.keys = _rating_sam_2_allKeys[_rating_sam_2_allKeys.length - 1].name;  // just the last key pressed
        rating_sam_2.rt = _rating_sam_2_allKeys[_rating_sam_2_allKeys.length - 1].rt;
        rating_sam_2.duration = _rating_sam_2_allKeys[_rating_sam_2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of SAM_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SAM_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SAM_2' ---
    for (const thisComponent of SAM_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('SAM_2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(rating_sam_2.corr, level);
    }
    psychoJS.experiment.addData('rating_sam_2.keys', rating_sam_2.keys);
    if (typeof rating_sam_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('rating_sam_2.rt', rating_sam_2.rt);
        psychoJS.experiment.addData('rating_sam_2.duration', rating_sam_2.duration);
        routineTimer.reset();
        }
    
    rating_sam_2.stop();
    // the Routine "SAM_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var SAM_3MaxDurationReached;
var _rating_sam_3_allKeys;
var SAM_3MaxDuration;
var SAM_3Components;
function SAM_3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SAM_3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    SAM_3Clock.reset();
    routineTimer.reset();
    SAM_3MaxDurationReached = false;
    // update component parameters for each repeat
    rating_sam_3.keys = undefined;
    rating_sam_3.rt = undefined;
    _rating_sam_3_allKeys = [];
    psychoJS.experiment.addData('SAM_3.started', globalClock.getTime());
    SAM_3MaxDuration = null
    // keep track of which components have finished
    SAM_3Components = [];
    SAM_3Components.push(question_sam_3);
    SAM_3Components.push(rating_sam_3);
    
    for (const thisComponent of SAM_3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function SAM_3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SAM_3' ---
    // get current time
    t = SAM_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *question_sam_3* updates
    if (t >= 0.0 && question_sam_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      question_sam_3.tStart = t;  // (not accounting for frame time here)
      question_sam_3.frameNStart = frameN;  // exact frame index
      
      question_sam_3.setAutoDraw(true);
    }
    
    
    // if question_sam_3 is active this frame...
    if (question_sam_3.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *rating_sam_3* updates
    if (t >= 0.0 && rating_sam_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rating_sam_3.tStart = t;  // (not accounting for frame time here)
      rating_sam_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { rating_sam_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { rating_sam_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { rating_sam_3.clearEvents(); });
    }
    
    // if rating_sam_3 is active this frame...
    if (rating_sam_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = rating_sam_3.getKeys({keyList: ['1','2','3','4','5','6','7','8','9'], waitRelease: false});
      _rating_sam_3_allKeys = _rating_sam_3_allKeys.concat(theseKeys);
      if (_rating_sam_3_allKeys.length > 0) {
        rating_sam_3.keys = _rating_sam_3_allKeys[_rating_sam_3_allKeys.length - 1].name;  // just the last key pressed
        rating_sam_3.rt = _rating_sam_3_allKeys[_rating_sam_3_allKeys.length - 1].rt;
        rating_sam_3.duration = _rating_sam_3_allKeys[_rating_sam_3_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of SAM_3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SAM_3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SAM_3' ---
    for (const thisComponent of SAM_3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('SAM_3.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(rating_sam_3.corr, level);
    }
    psychoJS.experiment.addData('rating_sam_3.keys', rating_sam_3.keys);
    if (typeof rating_sam_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('rating_sam_3.rt', rating_sam_3.rt);
        psychoJS.experiment.addData('rating_sam_3.duration', rating_sam_3.duration);
        routineTimer.reset();
        }
    
    rating_sam_3.stop();
    // the Routine "SAM_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
