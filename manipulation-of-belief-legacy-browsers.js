/******************************* 
 * Manipulation-Of-Belief *
 *******************************/


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
flowScheduler.add(instructionsRoutineBegin());
flowScheduler.add(instructionsRoutineEachFrame());
flowScheduler.add(instructionsRoutineEnd());
flowScheduler.add(preparationRoutineBegin());
flowScheduler.add(preparationRoutineEachFrame());
flowScheduler.add(preparationRoutineEnd());
const stimuliLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(stimuliLoopBegin(stimuliLoopScheduler));
flowScheduler.add(stimuliLoopScheduler);
flowScheduler.add(stimuliLoopEnd);





flowScheduler.add(questionnaireRoutineBegin());
flowScheduler.add(questionnaireRoutineEachFrame());
flowScheduler.add(questionnaireRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'variables/stimuli.csv', 'path': 'variables/stimuli.csv'},
    {'name': 'stimuli/sam-1.png', 'path': 'stimuli/sam-1.png'},
    {'name': 'stimuli/sam-2.png', 'path': 'stimuli/sam-2.png'},
    {'name': 'stimuli/sam-3.png', 'path': 'stimuli/sam-3.png'},
    {'name': 'variables/questionnaire_form.xlsx', 'path': 'variables/questionnaire_form.xlsx'},
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


var instructionsClock;
var text_norm;
var key_instruct;
var preparationClock;
var text_countdown;
var videoClock;
var video_stimuliClock;
var video_stimuli;
var text;
var skip_video;
var SAM_1Clock;
var question_sam_1;
var rating_sam_1;
var SAM_2Clock;
var question_sam_2;
var rating_sam_2;
var SAM_3Clock;
var question_sam_3;
var rating_sam_3;
var questionnaireClock;
var questionnaire_form;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  text_norm = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_norm',
    text: 'Any text\n\nincluding line breaks\n\nThis text component is white, so change the colour if you have a white background. It does not save the onset and offset time, but has been left justified with a wrap width of 1.8 norm units.\n\nPress the spacebar to continue',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], draggable: false, height: 0.1,  wrapWidth: 1.8, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_instruct = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from text_align
  // Code component set to Both
  text_norm.setAlignHoriz('left')
  // Initialize components for Routine "preparation"
  preparationClock = new util.Clock();
  text_countdown = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_countdown',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "video"
  videoClock = new util.Clock();
  // Run 'Begin Experiment' code from load_design
  /* Syntax Error: Fix Python code */
  video_stimuliClock = new util.Clock();
  video_stimuli = new visual.MovieStim({
    win: psychoJS.window,
    movie: null,
    name: 'video_stimuli',
    units: psychoJS.window.units,
    pos: [0, 0],
    anchor: 'center',
    size: null,
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
  
  skip_video = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
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
  
  // Initialize components for Routine "questionnaire"
  questionnaireClock = new util.Clock();
  questionnaire_form = new visual.Form({
    win : psychoJS.window, name:'questionnaire_form',
    items : 'variables/questionnaire_form.xlsx',
    textHeight : 0.03,
    font : 'Noto Sans',
    randomize : false,
    size : [1, 0.7],
    pos : [0, 0],
    style : 'dark',
    itemPadding : 0.05,
    depth : 0
  });
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var routineForceEnded;
var instructionsMaxDurationReached;
var _key_instruct_allKeys;
var instructionsMaxDuration;
var instructionsComponents;
function instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    instructionsClock.reset();
    routineTimer.reset();
    instructionsMaxDurationReached = false;
    // update component parameters for each repeat
    key_instruct.keys = undefined;
    key_instruct.rt = undefined;
    _key_instruct_allKeys = [];
    psychoJS.experiment.addData('instructions.started', globalClock.getTime());
    instructionsMaxDuration = null
    // keep track of which components have finished
    instructionsComponents = [];
    instructionsComponents.push(text_norm);
    instructionsComponents.push(key_instruct);
    
    instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions' ---
    // get current time
    t = instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_norm* updates
    if (t >= 0.0 && text_norm.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_norm.tStart = t;  // (not accounting for frame time here)
      text_norm.frameNStart = frameN;  // exact frame index
      
      text_norm.setAutoDraw(true);
    }
    
    
    // if text_norm is active this frame...
    if (text_norm.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_instruct* updates
    if (t >= 0.0 && key_instruct.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_instruct.tStart = t;  // (not accounting for frame time here)
      key_instruct.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_instruct.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_instruct.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_instruct.clearEvents(); });
    }
    
    // if key_instruct is active this frame...
    if (key_instruct.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_instruct.getKeys({keyList: 'space', waitRelease: false});
      _key_instruct_allKeys = _key_instruct_allKeys.concat(theseKeys);
      if (_key_instruct_allKeys.length > 0) {
        key_instruct.keys = _key_instruct_allKeys[0].name;  // just the first key pressed
        key_instruct.rt = _key_instruct_allKeys[0].rt;
        key_instruct.duration = _key_instruct_allKeys[0].duration;
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
    instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions' ---
    instructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('instructions.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_instruct.corr, level);
    }
    psychoJS.experiment.addData('key_instruct.keys', key_instruct.keys);
    if (typeof key_instruct.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_instruct.rt', key_instruct.rt);
        psychoJS.experiment.addData('key_instruct.duration', key_instruct.duration);
        routineTimer.reset();
        }
    
    key_instruct.stop();
    // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var preparationMaxDurationReached;
var preparationMaxDuration;
var preparationComponents;
function preparationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'preparation' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    preparationClock.reset(routineTimer.getTime());
    routineTimer.add(10.000000);
    preparationMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('preparation.started', globalClock.getTime());
    preparationMaxDuration = null
    // keep track of which components have finished
    preparationComponents = [];
    preparationComponents.push(text_countdown);
    
    preparationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function preparationRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'preparation' ---
    // get current time
    t = preparationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_countdown* updates
    if (t >= 0.0 && text_countdown.status === PsychoJS.Status.NOT_STARTED) {
      // update params
      text_countdown.setText((10 - Number.parseInt(t)).toString(), false);
      // keep track of start time/frame for later
      text_countdown.tStart = t;  // (not accounting for frame time here)
      text_countdown.frameNStart = frameN;  // exact frame index
      
      text_countdown.setAutoDraw(true);
    }
    
    
    // if text_countdown is active this frame...
    if (text_countdown.status === PsychoJS.Status.STARTED) {
      // update params
      text_countdown.setText((10 - Number.parseInt(t)).toString(), false);
    }
    
    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_countdown.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text_countdown.tStop = t;  // not accounting for scr refresh
      text_countdown.frameNStop = frameN;  // exact frame index
      // update status
      text_countdown.status = PsychoJS.Status.FINISHED;
      text_countdown.setAutoDraw(false);
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
    preparationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function preparationRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'preparation' ---
    preparationComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('preparation.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (preparationMaxDurationReached) {
        preparationClock.add(preparationMaxDuration);
    } else {
        preparationClock.add(10.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var stimuli;
function stimuliLoopBegin(stimuliLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    stimuli = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'variables/stimuli.csv',
      seed: undefined, name: 'stimuli'
    });
    psychoJS.experiment.addLoop(stimuli); // add the loop to the experiment
    currentLoop = stimuli;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    stimuli.forEach(function() {
      snapshot = stimuli.getSnapshot();
    
      stimuliLoopScheduler.add(importConditions(snapshot));
      stimuliLoopScheduler.add(videoRoutineBegin(snapshot));
      stimuliLoopScheduler.add(videoRoutineEachFrame());
      stimuliLoopScheduler.add(videoRoutineEnd(snapshot));
      stimuliLoopScheduler.add(SAM_1RoutineBegin(snapshot));
      stimuliLoopScheduler.add(SAM_1RoutineEachFrame());
      stimuliLoopScheduler.add(SAM_1RoutineEnd(snapshot));
      stimuliLoopScheduler.add(SAM_2RoutineBegin(snapshot));
      stimuliLoopScheduler.add(SAM_2RoutineEachFrame());
      stimuliLoopScheduler.add(SAM_2RoutineEnd(snapshot));
      stimuliLoopScheduler.add(SAM_3RoutineBegin(snapshot));
      stimuliLoopScheduler.add(SAM_3RoutineEachFrame());
      stimuliLoopScheduler.add(SAM_3RoutineEnd(snapshot));
      stimuliLoopScheduler.add(stimuliLoopEndIteration(stimuliLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function stimuliLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(stimuli);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function stimuliLoopEndIteration(scheduler, snapshot) {
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


var videoMaxDurationReached;
var _skip_video_allKeys;
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
    videoClock.reset();
    routineTimer.reset();
    videoMaxDurationReached = false;
    // update component parameters for each repeat
    video_stimuli.setMovie(video_file);
    text.setText(label_text);
    skip_video.keys = undefined;
    skip_video.rt = undefined;
    _skip_video_allKeys = [];
    psychoJS.experiment.addData('video.started', globalClock.getTime());
    videoMaxDuration = null
    // keep track of which components have finished
    videoComponents = [];
    videoComponents.push(video_stimuli);
    videoComponents.push(text);
    videoComponents.push(skip_video);
    
    videoComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function videoRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'video' ---
    // get current time
    t = videoClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *video_stimuli* updates
    if (t >= 0.0 && video_stimuli.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      video_stimuli.tStart = t;  // (not accounting for frame time here)
      video_stimuli.frameNStart = frameN;  // exact frame index
      
      video_stimuli.setAutoDraw(true);
      video_stimuli.play();
    }
    
    if (video_stimuli.status === PsychoJS.Status.FINISHED) {  // force-end the Routine
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
    
    
    // *skip_video* updates
    if (t >= 0.0 && skip_video.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      skip_video.tStart = t;  // (not accounting for frame time here)
      skip_video.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { skip_video.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { skip_video.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { skip_video.clearEvents(); });
    }
    
    // if skip_video is active this frame...
    if (skip_video.status === PsychoJS.Status.STARTED) {
      let theseKeys = skip_video.getKeys({keyList: 'space', waitRelease: false});
      _skip_video_allKeys = _skip_video_allKeys.concat(theseKeys);
      if (_skip_video_allKeys.length > 0) {
        skip_video.keys = _skip_video_allKeys[_skip_video_allKeys.length - 1].name;  // just the last key pressed
        skip_video.rt = _skip_video_allKeys[_skip_video_allKeys.length - 1].rt;
        skip_video.duration = _skip_video_allKeys[_skip_video_allKeys.length - 1].duration;
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
    videoComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function videoRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'video' ---
    videoComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('video.stopped', globalClock.getTime());
    video_stimuli.stop();  // ensure movie has stopped at end of Routine
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(skip_video.corr, level);
    }
    psychoJS.experiment.addData('skip_video.keys', skip_video.keys);
    if (typeof skip_video.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('skip_video.rt', skip_video.rt);
        psychoJS.experiment.addData('skip_video.duration', skip_video.duration);
        routineTimer.reset();
        }
    
    skip_video.stop();
    // the Routine "video" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
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
    
    SAM_1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    SAM_1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    SAM_1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    SAM_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    SAM_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    SAM_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    SAM_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    SAM_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    SAM_3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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


var questionnaireMaxDurationReached;
var questionnaireMaxDuration;
var questionnaireComponents;
function questionnaireRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'questionnaire' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    questionnaireClock.reset();
    routineTimer.reset();
    questionnaireMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('questionnaire.started', globalClock.getTime());
    questionnaireMaxDuration = null
    // keep track of which components have finished
    questionnaireComponents = [];
    questionnaireComponents.push(questionnaire_form);
    
    questionnaireComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function questionnaireRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'questionnaire' ---
    // get current time
    t = questionnaireClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *questionnaire_form* updates
    if (t >= 0.0 && questionnaire_form.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      questionnaire_form.tStart = t;  // (not accounting for frame time here)
      questionnaire_form.frameNStart = frameN;  // exact frame index
      
      questionnaire_form.setAutoDraw(true);
    }
    
    
    // if questionnaire_form is active this frame...
    if (questionnaire_form.status === PsychoJS.Status.STARTED) {
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
    questionnaireComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function questionnaireRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'questionnaire' ---
    questionnaireComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('questionnaire.stopped', globalClock.getTime());
    questionnaire_form.addDataToExp(psychoJS.experiment, 'rows');
    // the Routine "questionnaire" was not non-slip safe, so reset the non-slip timer
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
