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
flowScheduler.add(videoRoutineBegin());
flowScheduler.add(videoRoutineEachFrame());
flowScheduler.add(videoRoutineEnd());
flowScheduler.add(SAMRoutineBegin());
flowScheduler.add(SAMRoutineEachFrame());
flowScheduler.add(SAMRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'stimuli/18840567-hd_1920_1080_30fps.mp4', 'path': 'stimuli/18840567-hd_1920_1080_30fps.mp4'},
    {'name': 'stimuli/sam-1.png', 'path': 'stimuli/sam-1.png'},
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
var SAMClock;
var question;
var rating;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "video"
  videoClock = new util.Clock();
  video1Clock = new util.Clock();
  video1 = new visual.MovieStim({
    win: psychoJS.window,
    movie: 'stimuli/18840567-hd_1920_1080_30fps.mp4',
    name: 'video1',
    units: psychoJS.window.units,
    pos: [0, 0],
    anchor: 'center',
    size: [0.5, 0.5],
    ori: 0.0,
    opacity: null,
    loop: false,
    noAudio: false,
    depth: 0
  })
  // Initialize components for Routine "SAM"
  SAMClock = new util.Clock();
  question = new visual.ImageStim({
    win : psychoJS.window,
    name : 'question', units : undefined, 
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
  rating = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
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
    routineTimer.add(10.000000);
    videoMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('video.started', globalClock.getTime());
    videoMaxDuration = null
    // keep track of which components have finished
    videoComponents = [];
    videoComponents.push(video1);
    
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
    
    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (video1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      video1.tStop = t;  // not accounting for scr refresh
      video1.frameNStop = frameN;  // exact frame index
      // update status
      video1.status = PsychoJS.Status.FINISHED;
      video1.setAutoDraw(false);
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
        videoClock.add(10.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var SAMMaxDurationReached;
var _rating_allKeys;
var SAMMaxDuration;
var SAMComponents;
function SAMRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SAM' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    SAMClock.reset();
    routineTimer.reset();
    SAMMaxDurationReached = false;
    // update component parameters for each repeat
    rating.keys = undefined;
    rating.rt = undefined;
    _rating_allKeys = [];
    psychoJS.experiment.addData('SAM.started', globalClock.getTime());
    SAMMaxDuration = null
    // keep track of which components have finished
    SAMComponents = [];
    SAMComponents.push(question);
    SAMComponents.push(rating);
    
    for (const thisComponent of SAMComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function SAMRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SAM' ---
    // get current time
    t = SAMClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *question* updates
    if (t >= 0.0 && question.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      question.tStart = t;  // (not accounting for frame time here)
      question.frameNStart = frameN;  // exact frame index
      
      question.setAutoDraw(true);
    }
    
    
    // if question is active this frame...
    if (question.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *rating* updates
    if (t >= 0.0 && rating.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rating.tStart = t;  // (not accounting for frame time here)
      rating.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { rating.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { rating.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { rating.clearEvents(); });
    }
    
    // if rating is active this frame...
    if (rating.status === PsychoJS.Status.STARTED) {
      let theseKeys = rating.getKeys({keyList: ['1','2','3','4','5'], waitRelease: false});
      _rating_allKeys = _rating_allKeys.concat(theseKeys);
      if (_rating_allKeys.length > 0) {
        rating.keys = _rating_allKeys[_rating_allKeys.length - 1].name;  // just the last key pressed
        rating.rt = _rating_allKeys[_rating_allKeys.length - 1].rt;
        rating.duration = _rating_allKeys[_rating_allKeys.length - 1].duration;
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
    for (const thisComponent of SAMComponents)
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


function SAMRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SAM' ---
    for (const thisComponent of SAMComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('SAM.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(rating.corr, level);
    }
    psychoJS.experiment.addData('rating.keys', rating.keys);
    if (typeof rating.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('rating.rt', rating.rt);
        psychoJS.experiment.addData('rating.duration', rating.duration);
        routineTimer.reset();
        }
    
    rating.stop();
    // the Routine "SAM" was not non-slip safe, so reset the non-slip timer
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
