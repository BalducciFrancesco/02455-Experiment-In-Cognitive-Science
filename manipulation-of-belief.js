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
flowScheduler.add(r_instructionsRoutineBegin());
flowScheduler.add(r_instructionsRoutineEachFrame());
flowScheduler.add(r_instructionsRoutineEnd());
flowScheduler.add(r_baselineRoutineBegin());
flowScheduler.add(r_baselineRoutineEachFrame());
flowScheduler.add(r_baselineRoutineEnd());
const stimuliLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(stimuliLoopBegin(stimuliLoopScheduler));
flowScheduler.add(stimuliLoopScheduler);
flowScheduler.add(stimuliLoopEnd);








flowScheduler.add(r_final_questionnaireRoutineBegin());
flowScheduler.add(r_final_questionnaireRoutineEachFrame());
flowScheduler.add(r_final_questionnaireRoutineEnd());
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
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);

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

async function experimentInit() {
  // Initialize components for Routine "r_instructions"
  r_instructionsClock = new util.Clock();
  instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_text',
    text: "You’ll watch four short, content-friendly videos where each one has a label that either says “AI-generated” or “human-generated”.\n\nAfter each video, you’ll fill out a short questionnaire about your experience with this video.\n \nYou can stop and withdraw at any time if you feel uncomfortable or simply don’t want to continue.\n\nPress SPACE when you're ready.",
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
  instructions_text.setAlignHoriz('left')
  // Initialize components for Routine "r_baseline"
  r_baselineClock = new util.Clock();
  baseline_countdown = new visual.TextStim({
    win: psychoJS.window,
    name: 'baseline_countdown',
    text: '',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.5)], draggable: false, height: 0.1,  wrapWidth: 1.8, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  baseline_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'baseline_text',
    text: 'Please now wait still and relax while we measure the baseline for your heartbeat at rest.\n\nOnly good vibes :)',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], draggable: false, height: 0.1,  wrapWidth: 1.8, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Run 'Begin Experiment' code from text_align_2
  // Code component set to Both
  baseline_text.setAlignHoriz('left')
  // Initialize components for Routine "r_preparation"
  r_preparationClock = new util.Clock();
  // Run 'Begin Experiment' code from load_design
  /* Syntax Error: Fix Python code */
  video_nature_cue_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'video_nature_cue_text',
    text: '',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], draggable: false, height: 0.1,  wrapWidth: 1.8, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "r_fixation"
  r_fixationClock = new util.Clock();
  fixation_cross = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation_cross', 
    vertices: 'cross', size:[30, 30],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color([(- 0.1765), (- 0.1765), (- 0.1765)]), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: 0, 
    interpolate: true, 
  });
  
  // Initialize components for Routine "r_video"
  r_videoClock = new util.Clock();
  videoClock = new util.Clock();
  video = new visual.MovieStim({
    win: psychoJS.window,
    movie: null,
    name: 'video',
    units: 'norm',
    pos: [0, 0],
    anchor: 'center',
    size: [2.0, 2.0],
    ori: 0.0,
    opacity: null,
    loop: false,
    noAudio: false,
    depth: 0
  })
  // Initialize components for Routine "r_SAM_1"
  r_SAM_1Clock = new util.Clock();
  question_sam_1_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'question_sam_1_text',
    text: 'Press a button 1-5 to express how the last video made you feel about being \nunhappy / happy\n\n(1 = very unhappy, 5 = very happy)',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.5], draggable: false, height: 0.1,  wrapWidth: 1.8, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  question_sam_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'question_sam_1', units : 'norm', 
    image : 'stimuli/sam-1.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, (- 0.3)], 
    draggable: false,
    size : [1.3, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  rating_sam_1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "r_SAM_2"
  r_SAM_2Clock = new util.Clock();
  question_sam_2_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'question_sam_2_text',
    text: 'Press a button 1-5 to express how the last video made you feel about being \ncalm / excited\n\n(1 = very calm, 5 = very excited)',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.5], draggable: false, height: 0.1,  wrapWidth: 1.8, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  question_sam_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'question_sam_2', units : 'norm', 
    image : 'stimuli/sam-2.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, (- 0.3)], 
    draggable: false,
    size : [1.3, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  rating_sam_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "r_SAM_3"
  r_SAM_3Clock = new util.Clock();
  question_sam_3_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'question_sam_3_text',
    text: 'Press a button 1-5 to express how the last video made you feel about being \ncontrolled / incontrolled\n\n(1 = very controlled, 5 = very incontrolled)',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.5], draggable: false, height: 0.1,  wrapWidth: 1.8, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  question_sam_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'question_sam_3', units : 'norm', 
    image : 'stimuli/sam-3.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, (- 0.3)], 
    draggable: false,
    size : [1.3, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  rating_sam_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "r_focus_questionnaire"
  r_focus_questionnaireClock = new util.Clock();
  focus_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'focus_text',
    text: 'In general, how focused were you about what was happening on the screen when watching the previous video?',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.5], draggable: false, height: 0.1,  wrapWidth: 1.8, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  focus_slider = new visual.Slider({
    win: psychoJS.window, name: 'focus_slider',
    startValue: undefined,
    size: [1.0, 0.1], pos: [0, (- 0.4)], ori: 0.0, units: 'norm',
    labels: ["Not focused at all", "", "", "", "Very focused"], fontSize: 0.05, ticks: [1, 2, 3, 4, 5],
    granularity: 1.0, style: ["RATING"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Noto Sans', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  // Initialize components for Routine "r_final_questionnaire"
  r_final_questionnaireClock = new util.Clock();
  opinion_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'opinion_text',
    text: 'In general, what is your opinion on AI-generated visual contents (specifically AI-generated videos)?',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.5], draggable: false, height: 0.1,  wrapWidth: 1.8, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  opinion_slider = new visual.Slider({
    win: psychoJS.window, name: 'opinion_slider',
    startValue: undefined,
    size: [1.0, 0.1], pos: [0, (- 0.4)], ori: 0.0, units: 'norm',
    labels: ["I don't like them", "", "", "", "I really like them"], fontSize: 0.05, ticks: [1, 2, 3, 4, 5],
    granularity: 1.0, style: ["RATING"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Noto Sans', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function r_instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'r_instructions' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    r_instructionsClock.reset();
    routineTimer.reset();
    r_instructionsMaxDurationReached = false;
    // update component parameters for each repeat
    key_instruct.keys = undefined;
    key_instruct.rt = undefined;
    _key_instruct_allKeys = [];
    psychoJS.experiment.addData('r_instructions.started', globalClock.getTime());
    r_instructionsMaxDuration = null
    // keep track of which components have finished
    r_instructionsComponents = [];
    r_instructionsComponents.push(instructions_text);
    r_instructionsComponents.push(key_instruct);
    
    for (const thisComponent of r_instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function r_instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'r_instructions' ---
    // get current time
    t = r_instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructions_text* updates
    if (t >= 0.0 && instructions_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_text.tStart = t;  // (not accounting for frame time here)
      instructions_text.frameNStart = frameN;  // exact frame index
      
      instructions_text.setAutoDraw(true);
    }
    
    
    // if instructions_text is active this frame...
    if (instructions_text.status === PsychoJS.Status.STARTED) {
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
    for (const thisComponent of r_instructionsComponents)
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

function r_instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'r_instructions' ---
    for (const thisComponent of r_instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('r_instructions.stopped', globalClock.getTime());
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
    // the Routine "r_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function r_baselineRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'r_baseline' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    r_baselineClock.reset(routineTimer.getTime());
    routineTimer.add(120.000000);
    r_baselineMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('r_baseline.started', globalClock.getTime());
    r_baselineMaxDuration = null
    // keep track of which components have finished
    r_baselineComponents = [];
    r_baselineComponents.push(baseline_countdown);
    r_baselineComponents.push(baseline_text);
    
    for (const thisComponent of r_baselineComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function r_baselineRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'r_baseline' ---
    // get current time
    t = r_baselineClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *baseline_countdown* updates
    if (t >= 0.0 && baseline_countdown.status === PsychoJS.Status.NOT_STARTED) {
      // update params
      baseline_countdown.setText('{:02d}:{:02d}'.format(((120 - int(t)) // 60), ((120 - int(t)) % 60)), false);
      // keep track of start time/frame for later
      baseline_countdown.tStart = t;  // (not accounting for frame time here)
      baseline_countdown.frameNStart = frameN;  // exact frame index
      
      baseline_countdown.setAutoDraw(true);
    }
    
    
    // if baseline_countdown is active this frame...
    if (baseline_countdown.status === PsychoJS.Status.STARTED) {
      // update params
      baseline_countdown.setText('{:02d}:{:02d}'.format(((120 - int(t)) // 60), ((120 - int(t)) % 60)), false);
    }
    
    frameRemains = 0.0 + 120 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (baseline_countdown.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      baseline_countdown.tStop = t;  // not accounting for scr refresh
      baseline_countdown.frameNStop = frameN;  // exact frame index
      // update status
      baseline_countdown.status = PsychoJS.Status.FINISHED;
      baseline_countdown.setAutoDraw(false);
    }
    
    
    // *baseline_text* updates
    if (t >= 0.0 && baseline_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      baseline_text.tStart = t;  // (not accounting for frame time here)
      baseline_text.frameNStart = frameN;  // exact frame index
      
      baseline_text.setAutoDraw(true);
    }
    
    
    // if baseline_text is active this frame...
    if (baseline_text.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 120 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (baseline_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      baseline_text.tStop = t;  // not accounting for scr refresh
      baseline_text.frameNStop = frameN;  // exact frame index
      // update status
      baseline_text.status = PsychoJS.Status.FINISHED;
      baseline_text.setAutoDraw(false);
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
    for (const thisComponent of r_baselineComponents)
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

function r_baselineRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'r_baseline' ---
    for (const thisComponent of r_baselineComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('r_baseline.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (r_baselineMaxDurationReached) {
        r_baselineClock.add(r_baselineMaxDuration);
    } else {
        r_baselineClock.add(120.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

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
    for (const thisStimulus of stimuli) {
      snapshot = stimuli.getSnapshot();
      stimuliLoopScheduler.add(importConditions(snapshot));
      stimuliLoopScheduler.add(r_preparationRoutineBegin(snapshot));
      stimuliLoopScheduler.add(r_preparationRoutineEachFrame());
      stimuliLoopScheduler.add(r_preparationRoutineEnd(snapshot));
      stimuliLoopScheduler.add(r_fixationRoutineBegin(snapshot));
      stimuliLoopScheduler.add(r_fixationRoutineEachFrame());
      stimuliLoopScheduler.add(r_fixationRoutineEnd(snapshot));
      stimuliLoopScheduler.add(r_videoRoutineBegin(snapshot));
      stimuliLoopScheduler.add(r_videoRoutineEachFrame());
      stimuliLoopScheduler.add(r_videoRoutineEnd(snapshot));
      stimuliLoopScheduler.add(r_SAM_1RoutineBegin(snapshot));
      stimuliLoopScheduler.add(r_SAM_1RoutineEachFrame());
      stimuliLoopScheduler.add(r_SAM_1RoutineEnd(snapshot));
      stimuliLoopScheduler.add(r_SAM_2RoutineBegin(snapshot));
      stimuliLoopScheduler.add(r_SAM_2RoutineEachFrame());
      stimuliLoopScheduler.add(r_SAM_2RoutineEnd(snapshot));
      stimuliLoopScheduler.add(r_SAM_3RoutineBegin(snapshot));
      stimuliLoopScheduler.add(r_SAM_3RoutineEachFrame());
      stimuliLoopScheduler.add(r_SAM_3RoutineEnd(snapshot));
      stimuliLoopScheduler.add(r_focus_questionnaireRoutineBegin(snapshot));
      stimuliLoopScheduler.add(r_focus_questionnaireRoutineEachFrame());
      stimuliLoopScheduler.add(r_focus_questionnaireRoutineEnd(snapshot));
      stimuliLoopScheduler.add(stimuliLoopEndIteration(stimuliLoopScheduler, snapshot));
    }
    
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

function r_preparationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'r_preparation' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    r_preparationClock.reset(routineTimer.getTime());
    routineTimer.add(5.000000);
    r_preparationMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('r_preparation.started', globalClock.getTime());
    r_preparationMaxDuration = null
    // keep track of which components have finished
    r_preparationComponents = [];
    r_preparationComponents.push(video_nature_cue_text);
    
    for (const thisComponent of r_preparationComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function r_preparationRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'r_preparation' ---
    // get current time
    t = r_preparationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *video_nature_cue_text* updates
    if (t >= 0.0 && video_nature_cue_text.status === PsychoJS.Status.NOT_STARTED) {
      // update params
      video_nature_cue_text.setText((((("The next video is going to be " + "\n") + label_text.toString()) + "\n\n") + (5 - Number.parseInt(t)).toString()), false);
      // keep track of start time/frame for later
      video_nature_cue_text.tStart = t;  // (not accounting for frame time here)
      video_nature_cue_text.frameNStart = frameN;  // exact frame index
      
      video_nature_cue_text.setAutoDraw(true);
    }
    
    
    // if video_nature_cue_text is active this frame...
    if (video_nature_cue_text.status === PsychoJS.Status.STARTED) {
      // update params
      video_nature_cue_text.setText((((("The next video is going to be " + "\n") + label_text.toString()) + "\n\n") + (5 - Number.parseInt(t)).toString()), false);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (video_nature_cue_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      video_nature_cue_text.tStop = t;  // not accounting for scr refresh
      video_nature_cue_text.frameNStop = frameN;  // exact frame index
      // update status
      video_nature_cue_text.status = PsychoJS.Status.FINISHED;
      video_nature_cue_text.setAutoDraw(false);
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
    for (const thisComponent of r_preparationComponents)
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

function r_preparationRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'r_preparation' ---
    for (const thisComponent of r_preparationComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('r_preparation.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (r_preparationMaxDurationReached) {
        r_preparationClock.add(r_preparationMaxDuration);
    } else {
        r_preparationClock.add(5.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function r_fixationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'r_fixation' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    r_fixationClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    r_fixationMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('r_fixation.started', globalClock.getTime());
    r_fixationMaxDuration = null
    // keep track of which components have finished
    r_fixationComponents = [];
    r_fixationComponents.push(fixation_cross);
    
    for (const thisComponent of r_fixationComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function r_fixationRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'r_fixation' ---
    // get current time
    t = r_fixationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation_cross* updates
    if (t >= 0.0 && fixation_cross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_cross.tStart = t;  // (not accounting for frame time here)
      fixation_cross.frameNStart = frameN;  // exact frame index
      
      fixation_cross.setAutoDraw(true);
    }
    
    
    // if fixation_cross is active this frame...
    if (fixation_cross.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (fixation_cross.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      fixation_cross.tStop = t;  // not accounting for scr refresh
      fixation_cross.frameNStop = frameN;  // exact frame index
      // update status
      fixation_cross.status = PsychoJS.Status.FINISHED;
      fixation_cross.setAutoDraw(false);
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
    for (const thisComponent of r_fixationComponents)
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

function r_fixationRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'r_fixation' ---
    for (const thisComponent of r_fixationComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('r_fixation.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (r_fixationMaxDurationReached) {
        r_fixationClock.add(r_fixationMaxDuration);
    } else {
        r_fixationClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function r_videoRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'r_video' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    r_videoClock.reset(routineTimer.getTime());
    routineTimer.add(120.000000);
    r_videoMaxDurationReached = false;
    // update component parameters for each repeat
    video.setMovie(video_file);
    psychoJS.experiment.addData('r_video.started', globalClock.getTime());
    r_videoMaxDuration = null
    // keep track of which components have finished
    r_videoComponents = [];
    r_videoComponents.push(video);
    
    for (const thisComponent of r_videoComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function r_videoRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'r_video' ---
    // get current time
    t = r_videoClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *video* updates
    if (t >= 0.0 && video.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      video.tStart = t;  // (not accounting for frame time here)
      video.frameNStart = frameN;  // exact frame index
      
      video.setAutoDraw(true);
      video.play();
    }
    
    frameRemains = 0.0 + 120 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (video.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      video.tStop = t;  // not accounting for scr refresh
      video.frameNStop = frameN;  // exact frame index
      // update status
      video.status = PsychoJS.Status.FINISHED;
      video.setAutoDraw(false);
    }
    
    if (video.status === PsychoJS.Status.FINISHED) {  // force-end the Routine
        continueRoutine = false;
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
    for (const thisComponent of r_videoComponents)
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

function r_videoRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'r_video' ---
    for (const thisComponent of r_videoComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('r_video.stopped', globalClock.getTime());
    video.stop();  // ensure movie has stopped at end of Routine
    if (routineForceEnded) {
        routineTimer.reset();} else if (r_videoMaxDurationReached) {
        r_videoClock.add(r_videoMaxDuration);
    } else {
        r_videoClock.add(120.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function r_SAM_1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'r_SAM_1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    r_SAM_1Clock.reset();
    routineTimer.reset();
    r_SAM_1MaxDurationReached = false;
    // update component parameters for each repeat
    rating_sam_1.keys = undefined;
    rating_sam_1.rt = undefined;
    _rating_sam_1_allKeys = [];
    psychoJS.experiment.addData('r_SAM_1.started', globalClock.getTime());
    r_SAM_1MaxDuration = null
    // keep track of which components have finished
    r_SAM_1Components = [];
    r_SAM_1Components.push(question_sam_1_text);
    r_SAM_1Components.push(question_sam_1);
    r_SAM_1Components.push(rating_sam_1);
    
    for (const thisComponent of r_SAM_1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function r_SAM_1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'r_SAM_1' ---
    // get current time
    t = r_SAM_1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *question_sam_1_text* updates
    if (t >= 0.0 && question_sam_1_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      question_sam_1_text.tStart = t;  // (not accounting for frame time here)
      question_sam_1_text.frameNStart = frameN;  // exact frame index
      
      question_sam_1_text.setAutoDraw(true);
    }
    
    
    // if question_sam_1_text is active this frame...
    if (question_sam_1_text.status === PsychoJS.Status.STARTED) {
    }
    
    
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
      let theseKeys = rating_sam_1.getKeys({keyList: ['1','2','3','4','5'], waitRelease: false});
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
    for (const thisComponent of r_SAM_1Components)
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

function r_SAM_1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'r_SAM_1' ---
    for (const thisComponent of r_SAM_1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('r_SAM_1.stopped', globalClock.getTime());
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
    // the Routine "r_SAM_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function r_SAM_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'r_SAM_2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    r_SAM_2Clock.reset();
    routineTimer.reset();
    r_SAM_2MaxDurationReached = false;
    // update component parameters for each repeat
    rating_sam_2.keys = undefined;
    rating_sam_2.rt = undefined;
    _rating_sam_2_allKeys = [];
    psychoJS.experiment.addData('r_SAM_2.started', globalClock.getTime());
    r_SAM_2MaxDuration = null
    // keep track of which components have finished
    r_SAM_2Components = [];
    r_SAM_2Components.push(question_sam_2_text);
    r_SAM_2Components.push(question_sam_2);
    r_SAM_2Components.push(rating_sam_2);
    
    for (const thisComponent of r_SAM_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function r_SAM_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'r_SAM_2' ---
    // get current time
    t = r_SAM_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *question_sam_2_text* updates
    if (t >= 0.0 && question_sam_2_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      question_sam_2_text.tStart = t;  // (not accounting for frame time here)
      question_sam_2_text.frameNStart = frameN;  // exact frame index
      
      question_sam_2_text.setAutoDraw(true);
    }
    
    
    // if question_sam_2_text is active this frame...
    if (question_sam_2_text.status === PsychoJS.Status.STARTED) {
    }
    
    
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
      let theseKeys = rating_sam_2.getKeys({keyList: ['1','2','3','4','5'], waitRelease: false});
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
    for (const thisComponent of r_SAM_2Components)
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

function r_SAM_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'r_SAM_2' ---
    for (const thisComponent of r_SAM_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('r_SAM_2.stopped', globalClock.getTime());
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
    // the Routine "r_SAM_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function r_SAM_3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'r_SAM_3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    r_SAM_3Clock.reset();
    routineTimer.reset();
    r_SAM_3MaxDurationReached = false;
    // update component parameters for each repeat
    rating_sam_3.keys = undefined;
    rating_sam_3.rt = undefined;
    _rating_sam_3_allKeys = [];
    psychoJS.experiment.addData('r_SAM_3.started', globalClock.getTime());
    r_SAM_3MaxDuration = null
    // keep track of which components have finished
    r_SAM_3Components = [];
    r_SAM_3Components.push(question_sam_3_text);
    r_SAM_3Components.push(question_sam_3);
    r_SAM_3Components.push(rating_sam_3);
    
    for (const thisComponent of r_SAM_3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function r_SAM_3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'r_SAM_3' ---
    // get current time
    t = r_SAM_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *question_sam_3_text* updates
    if (t >= 0.0 && question_sam_3_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      question_sam_3_text.tStart = t;  // (not accounting for frame time here)
      question_sam_3_text.frameNStart = frameN;  // exact frame index
      
      question_sam_3_text.setAutoDraw(true);
    }
    
    
    // if question_sam_3_text is active this frame...
    if (question_sam_3_text.status === PsychoJS.Status.STARTED) {
    }
    
    
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
      let theseKeys = rating_sam_3.getKeys({keyList: ['1','2','3','4','5'], waitRelease: false});
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
    for (const thisComponent of r_SAM_3Components)
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

function r_SAM_3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'r_SAM_3' ---
    for (const thisComponent of r_SAM_3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('r_SAM_3.stopped', globalClock.getTime());
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
    // the Routine "r_SAM_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function r_focus_questionnaireRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'r_focus_questionnaire' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    r_focus_questionnaireClock.reset();
    routineTimer.reset();
    r_focus_questionnaireMaxDurationReached = false;
    // update component parameters for each repeat
    focus_slider.reset()
    psychoJS.experiment.addData('r_focus_questionnaire.started', globalClock.getTime());
    r_focus_questionnaireMaxDuration = null
    // keep track of which components have finished
    r_focus_questionnaireComponents = [];
    r_focus_questionnaireComponents.push(focus_text);
    r_focus_questionnaireComponents.push(focus_slider);
    
    for (const thisComponent of r_focus_questionnaireComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function r_focus_questionnaireRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'r_focus_questionnaire' ---
    // get current time
    t = r_focus_questionnaireClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *focus_text* updates
    if (t >= 0.0 && focus_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      focus_text.tStart = t;  // (not accounting for frame time here)
      focus_text.frameNStart = frameN;  // exact frame index
      
      focus_text.setAutoDraw(true);
    }
    
    
    // if focus_text is active this frame...
    if (focus_text.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *focus_slider* updates
    if (t >= 0.0 && focus_slider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      focus_slider.tStart = t;  // (not accounting for frame time here)
      focus_slider.frameNStart = frameN;  // exact frame index
      
      focus_slider.setAutoDraw(true);
    }
    
    
    // if focus_slider is active this frame...
    if (focus_slider.status === PsychoJS.Status.STARTED) {
    }
    
    
    // Check focus_slider for response to end Routine
    if (focus_slider.getRating() !== undefined && focus_slider.status === PsychoJS.Status.STARTED) {
      continueRoutine = false; }
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
    for (const thisComponent of r_focus_questionnaireComponents)
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

function r_focus_questionnaireRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'r_focus_questionnaire' ---
    for (const thisComponent of r_focus_questionnaireComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('r_focus_questionnaire.stopped', globalClock.getTime());
    psychoJS.experiment.addData('focus_slider.response', focus_slider.getRating());
    psychoJS.experiment.addData('focus_slider.rt', focus_slider.getRT());
    // the Routine "r_focus_questionnaire" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function r_final_questionnaireRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'r_final_questionnaire' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    r_final_questionnaireClock.reset();
    routineTimer.reset();
    r_final_questionnaireMaxDurationReached = false;
    // update component parameters for each repeat
    opinion_slider.reset()
    psychoJS.experiment.addData('r_final_questionnaire.started', globalClock.getTime());
    r_final_questionnaireMaxDuration = null
    // keep track of which components have finished
    r_final_questionnaireComponents = [];
    r_final_questionnaireComponents.push(opinion_text);
    r_final_questionnaireComponents.push(opinion_slider);
    
    for (const thisComponent of r_final_questionnaireComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function r_final_questionnaireRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'r_final_questionnaire' ---
    // get current time
    t = r_final_questionnaireClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *opinion_text* updates
    if (t >= 0.0 && opinion_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      opinion_text.tStart = t;  // (not accounting for frame time here)
      opinion_text.frameNStart = frameN;  // exact frame index
      
      opinion_text.setAutoDraw(true);
    }
    
    
    // if opinion_text is active this frame...
    if (opinion_text.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *opinion_slider* updates
    if (t >= 0.0 && opinion_slider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      opinion_slider.tStart = t;  // (not accounting for frame time here)
      opinion_slider.frameNStart = frameN;  // exact frame index
      
      opinion_slider.setAutoDraw(true);
    }
    
    
    // if opinion_slider is active this frame...
    if (opinion_slider.status === PsychoJS.Status.STARTED) {
    }
    
    
    // Check opinion_slider for response to end Routine
    if (opinion_slider.getRating() !== undefined && opinion_slider.status === PsychoJS.Status.STARTED) {
      continueRoutine = false; }
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
    for (const thisComponent of r_final_questionnaireComponents)
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

function r_final_questionnaireRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'r_final_questionnaire' ---
    for (const thisComponent of r_final_questionnaireComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('r_final_questionnaire.stopped', globalClock.getTime());
    psychoJS.experiment.addData('opinion_slider.response', opinion_slider.getRating());
    psychoJS.experiment.addData('opinion_slider.rt', opinion_slider.getRT());
    // the Routine "r_final_questionnaire" was not non-slip safe, so reset the non-slip timer
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
