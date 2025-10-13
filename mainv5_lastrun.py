#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2025.1.1),
    on 八月 19, 2025, at 18:17
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

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from prepare_code
from PIL import Image
import datetime
#Max mouse debounce timeout(s)
#Google up the meaning of debounce!
mouse_debounce_timeout = 1
#Max mouse debounce timeout(s)
#Fuck you google!
inoculation_debounce_timeout = 15 #yes fuck you google.
#inoculation/non-inoculation share the same scale ratio
scale_stim_maxX_ratio = 0.8
scale_stim_maxY_ratio = 0.8
#thumbnail all share this ratio
thumbnail_to_screen_scale_factor = 0.35
#button use these x, y offset(to screen edge), and size ratio
continue_btm_x_offset_ratio = 0.02742
continue_btm_y_offset_ratio = 0.05442
continue_btm_size_ratio = 0.104
#form can be tricky as it's still bounded by height
form_offset_left = 0.06125
form_offset_right = 0.06125
form_offset_top = 0.08
form_offset_bottom = 0.22
form_related_ratio = 1.7777777777777777777777777777777777777777777
#dv_short/long
dv_x_offset = 0
dv_yshort_offset = -0.18
dv_ylong_offset = -0.285
dv_h_ratio = 0.06
dv_wshort_ratio = 0.759375
dv_wlong_ratio = 0.84375
#resp_banner
resp_banner_h_ratio = 0.065
resp_banner_y_offset = 0.4
#attitude_bg
att_bg_ratio = 0.86
att_bg_y_offset = -0.1455
#we_bg
we_bg_ratio = 0.91125
we_bg_y_offset = -0.13
# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2025.1.1'
expName = 'mainv5'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': '69',
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
_winSize = [1536, 864]
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
        originPath='C:\\Users\\Research10Zumi\\Desktop\\main_experiment\\mainv5_lastrun.py',
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
            monitor='testMonitor', color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='pix',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [1.0000, 1.0000, 1.0000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'pix'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Preparing... Please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
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
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
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
            backend='ioHub',
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
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
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
    
    # --- Initialize components for Routine "prepare_everything" ---
    # Run 'Begin Experiment' code from prepare_code
    try:
        participant_num = int(expInfo['participant'])
    except ValueError:
        participant_num = 0  # 若輸入非數字，則預設為 0
    
    counterbalance_order = [
        [1,2,24,3,23,4,22,5,21,6,20,7,19,8,18,9,17,10,16,11,15,12,14,13],
        [2,3,1,4,24,5,23,6,22,7,21,8,20,9,19,10,18,11,17,12,16,13,15,14],
        [3,4,2,5,1,6,24,7,23,8,22,9,21,10,20,11,19,12,18,13,17,14,16,15],
        [4,5,3,6,2,7,1,8,24,9,23,10,22,11,21,12,20,13,19,14,18,15,17,16],
        [5,6,4,7,3,8,2,9,1,10,24,11,23,12,22,13,21,14,20,15,19,16,18,17],
        [6,7,5,8,4,9,3,10,2,11,1,12,24,13,23,14,22,15,21,16,20,17,19,18],
        [7,8,6,9,5,10,4,11,3,12,2,13,1,14,24,15,23,16,22,17,21,18,20,19],
        [8,9,7,10,6,11,5,12,4,13,3,14,2,15,1,16,24,17,23,18,22,19,21,20],
        [9,10,8,11,7,12,6,13,5,14,4,15,3,16,2,17,1,18,24,19,23,20,22,21],
        [10,11,9,12,8,13,7,14,6,15,5,16,4,17,3,18,2,19,1,20,24,21,23,22],
        [11,12,10,13,9,14,8,15,7,16,6,17,5,18,4,19,3,20,2,21,1,22,24,23],
        [12,13,11,14,10,15,9,16,8,17,7,18,6,19,5,20,4,21,3,22,2,23,1,24],
        [13,14,12,15,11,16,10,17,9,18,8,19,7,20,6,21,5,22,4,23,3,24,2,1],
        [14,15,13,16,12,17,11,18,10,19,9,20,8,21,7,22,6,23,5,24,4,1,3,2],
        [15,16,14,17,13,18,12,19,11,20,10,21,9,22,8,23,7,24,6,1,5,2,4,3],
        [16,17,15,18,14,19,13,20,12,21,11,22,10,23,9,24,8,1,7,2,6,3,5,4],
        [17,18,16,19,15,20,14,21,13,22,12,23,11,24,10,1,9,2,8,3,7,4,6,5],
        [18,19,17,20,16,21,15,22,14,23,13,24,12,1,11,2,10,3,9,4,8,5,7,6],
        [19,20,18,21,17,22,16,23,15,24,14,1,13,2,12,3,11,4,10,5,9,6,8,7],
        [20,21,19,22,18,23,17,24,16,1,15,2,14,3,13,4,12,5,11,6,10,7,9,8],
        [21,22,20,23,19,24,18,1,17,2,16,3,15,4,14,5,13,6,12,7,11,8,10,9],
        [22,23,21,24,20,1,19,2,18,3,17,4,16,5,15,6,14,7,13,8,12,9,11,10],
        [23,24,22,1,21,2,20,3,19,4,18,5,17,6,16,7,15,8,14,9,13,10,12,11],
        [24,1,23,2,22,3,21,4,20,5,19,6,18,7,17,8,16,9,15,10,14,11,13,12]
    ]
    
    resp_counterbalance = [
        [1,2,3],
        [1,3,2],
        [3,1,2],
        [3,2,1],
        [2,3,1],
        [2,1,3]
    ]
    
    if participant_num < 1:
        raise ValueError(f"WTF我們拿到了受試者號碼{participant_num}")
    
    # generate countrbl length for 2 further use, controls how many trials a participant will do
    counterbalance_len  = len(counterbalance_order)
    
    #also resp_order len i guess
    resp_order_cb_len = len(resp_counterbalance)
    
    # 1. Generate trial_order, a list for controlling participants' stim disp order
    part_cb_index = (participant_num - 1) % counterbalance_len 
    
    raw_order = counterbalance_order[part_cb_index]
    
    trial_order = [i-1 for i in raw_order]
    
    # 2. Generate resp_order, a list that determines the order of 3 responses
    # the number 6 is determined by counterbalancing 3 responces's order
    # We try to allocate those '6s' to each participants
    # if the participant have to go through a multiple of 6 times of trials,
    # then the 6s is happily distributed to each participants evenly
    # however that's not all the case, for example, say 32 trials, not a multiple of 6
    # then we'll have to be smart and "guess" where should each participant start,
    # accroding to resp_counterbalance, so the overall counterbalance is achieved.
    # To do this, we calculate... just see the math won't you?
    # After all this is just a reminder for myself in case I start dobuting myself for no reason
    total_offset = (counterbalance_len % resp_order_cb_len) * (participant_num - 1)
    offset_target = (1 + total_offset) % resp_order_cb_len
    # ok now we have offset target (that tells us where does the resp index start... yet)
    # next we'll generate a list of index that's supposed to point to the
    # response order list index, and generate the full list for later use
    resp_order_list = [resp_counterbalance[((offset_target - 1 + i) % resp_order_cb_len)] for i in range(counterbalance_len)]
    
    # 1st particiant has been subjected to "inoculation"
    inoculation_switch = True if participant_num % 2 == 1 else False
    
    #le screen size
    screenX, screenY = win.size
    rel_w = (screenX/screenY)/2
    
    scale_stim_maxX = screenX * scale_stim_maxX_ratio
    scale_stim_maxY = screenY * scale_stim_maxY_ratio
    
    print(f"Participant: {participant_num}, Sequence: {trial_order}, offset_target: {offset_target}, inoculation_switch: {inoculation_switch}, resp_order_list: {resp_order_list}")
    
    #inoculation area calculation
    with Image.open('text1.png') as im:
        stim_pic_sizeX_inopic, stim_pic_sizeY_inopic = im.size
    stim_heightX_inopic = scale_stim_maxY * (stim_pic_sizeX_inopic / stim_pic_sizeY_inopic)
    stim_heightY_inopic = scale_stim_maxY
    if stim_heightX_inopic > scale_stim_maxX:
        stim_heightY_inopic = stim_heightY_inopic / (stim_heightX_inopic / scale_stim_maxX)
        stim_heightX_inopic = scale_stim_maxX
        
    #non-inoculation area calculation
    with Image.open('text44.png') as im:
        stim_pic_sizeX_noninopic, stim_pic_sizeY_noninopic = im.size
    stim_heightX_noninopic = scale_stim_maxY * (stim_pic_sizeX_noninopic / stim_pic_sizeY_noninopic)
    stim_heightY_noninopic = scale_stim_maxY
    if stim_heightX_noninopic > scale_stim_maxX:
        stim_heightY_noninopic = stim_heightY_noninopic / (stim_heightX_noninopic / scale_stim_maxX)
        stim_heightX_noninopic = scale_stim_maxX
    
    with Image.open('normal_next_btn.png') as im:
        btm_orig_size_x, btm_orig_size_y = im.size
    btm_pic_ratio = btm_orig_size_x/btm_orig_size_y
    btm_size_w = screenX * continue_btm_size_ratio
    btm_size_h = btm_size_w / btm_pic_ratio
    btm_x = screenX/2 - (continue_btm_x_offset_ratio * screenX + btm_size_w/2)
    btm_y = -(screenY/2 - (continue_btm_y_offset_ratio * screenY + btm_size_h/2))
    
    form_x = 0 #center aligned
    form_y = (form_offset_bottom - form_offset_top) * screenY/2
    form_w = (1 - form_offset_left - form_offset_right) * screenX
    form_h = (1 - form_offset_bottom - form_offset_top) * screenY
    
    form_xHeight = 0
    form_yHeight = form_y / screenY
    form_wHeight = form_w / screenX * (screenX/screenY)
    form_hHeight = form_h / screenY
    
    dv_x = dv_x_offset * screenX
    dv_yshort = dv_yshort_offset * screenY
    dv_ylong = dv_ylong_offset * screenY
    dv_wshort = dv_wshort_ratio * screenX
    dv_wlong = dv_wlong_ratio * screenX
    dv_h = dv_h_ratio * screenY
    
    resp_banner_h = resp_banner_h_ratio * screenY
    resp_banner_y = resp_banner_y_offset * screenY
    
    with Image.open('path3.png') as im:
        att_bg_size_x, att_bg_size_y = im.size
    att_bg_pic_ratio = att_bg_size_x/att_bg_size_y
    att_bg_w = att_bg_ratio * screenX
    att_bg_h = att_bg_w / att_bg_pic_ratio
    att_bg_y = att_bg_y_offset * screenY
    
    with Image.open('emoticon_all.png') as im:
        we_bg_size_x, we_bg_size_y = im.size
    we_bg_pic_ratio = we_bg_size_x/we_bg_size_y
    we_bg_w = we_bg_ratio * screenX
    we_bg_h = we_bg_w / we_bg_pic_ratio
    we_bg_y = we_bg_y_offset * screenY
    
    print(f"att_bg_w:{att_bg_w},att_bg_h:{att_bg_h},att_bg_y:{att_bg_y}")
    
    print(f"form_x:{form_x},form_y:{form_y},form_w:{form_w},form_h:{form_h}")
    print(f"form_xHeight:{form_xHeight},form_yHeight:{form_yHeight},form_wHeight:{form_wHeight},form_hHeight:{form_hHeight}")
    
    
    
    # --- Initialize components for Routine "Introduction" ---
    text_norm69 = visual.TextStim(win=win, name='text_norm69',
        text='本實驗歷時30分鐘\n請根據指示進行作答',
        font='Noto Sans TC',
        units='height', pos=(0, 0), draggable=False, height=0.06, wrapWidth=15.0, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    btn1_img = visual.ImageStim(
        win=win,
        name='btn1_img', units='pix', 
        image='normal_next_btn.png', mask=None, anchor='center',
        ori=0.0, pos=(btm_x,btm_y), draggable=False, size=(btm_size_w,btm_size_h),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    mouse1 = event.Mouse(win=win)
    x, y = [None, None]
    mouse1.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "Demographic_Form" ---
    win.allowStencil = True
    demog_form = visual.Form(win=win, name='demog_form',
        items='demographics_form_lookup.csv',
        textHeight=0.03,
        font='Noto Sans TC',
        randomize=False,
        style='custom...',
        fillColor=[1.0000, 1.0000, 1.0000], borderColor=[-1.0000, -1.0000, -1.0000], itemColor='black', 
        responseColor='black', markerColor='black', colorSpace='rgb', 
        size=(form_wHeight,form_hHeight),
        pos=(form_xHeight,form_yHeight),
        itemPadding=0.05,
        depth=0
    )
    btn2_img = visual.ImageStim(
        win=win,
        name='btn2_img', units='pix', 
        image='normal_next_btn.png', mask=None, anchor='center',
        ori=0.0, pos=(btm_x,btm_y), draggable=False, size=(btm_size_w,btm_size_h),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    mouse2 = event.Mouse(win=win)
    x, y = [None, None]
    mouse2.mouseClock = core.Clock()
    pre_indicator_3 = visual.TextStim(win=win, name='pre_indicator_3',
        text='[請填寫表單]',
        font='Noto Sans TC',
        units='height', pos=((-0.02 + btm_x/screenX) * (screenX/screenY), btm_y/screenY), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "Ino_Intro" ---
    text_norm_6 = visual.TextStim(win=win, name='text_norm_6',
        text='接下來將會提供閱讀材料，請仔細閱讀以便後續實驗進行\n\n閱讀材料顯示後十五秒，「繼續」鍵才會顯示',
        font='Noto Sans TC',
        units='height', pos=(0, 0), draggable=False, height=0.06, wrapWidth=69.0, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    btn69_img = visual.ImageStim(
        win=win,
        name='btn69_img', units='pix', 
        image='normal_next_btn.png', mask=None, anchor='center',
        ori=0.0, pos=(btm_x,btm_y), draggable=False, size=(btm_size_w,btm_size_h),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    mouse69 = event.Mouse(win=win)
    x, y = [None, None]
    mouse69.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "Inoculation" ---
    btn4_img = visual.ImageStim(
        win=win,
        name='btn4_img', 
        image='normal_next_btn.png', mask=None, anchor='center',
        ori=0.0, pos=(btm_x,btm_y), draggable=False, size=(btm_size_w,btm_size_h),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    mouse4 = event.Mouse(win=win)
    x, y = [None, None]
    mouse4.mouseClock = core.Clock()
    image = visual.ImageStim(
        win=win,
        name='image', units='pix', 
        image='text1.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(stim_heightX_inopic, stim_heightY_inopic),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "NonInoculation" ---
    btn5_img = visual.ImageStim(
        win=win,
        name='btn5_img', 
        image='normal_next_btn.png', mask=None, anchor='center',
        ori=0.0, pos=(btm_x,btm_y), draggable=False, size=(btm_size_w,btm_size_h),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    mouse5 = event.Mouse(win=win)
    x, y = [None, None]
    mouse5.mouseClock = core.Clock()
    image_2 = visual.ImageStim(
        win=win,
        name='image_2', units='pix', 
        image='text44.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(stim_heightX_noninopic, stim_heightY_noninopic),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "Review_Intro" ---
    text_norm_7 = visual.TextStim(win=win, name='text_norm_7',
        text='接下來會進行「資訊說明」的簡單複習 \n閱讀完題目請對A、B選項進行選擇\n作答完畢3秒後會公布答案\n充分理解完後請按「繼續」鍵',
        font='Noto Sans TC',
        units='height', pos=(0, 0), draggable=False, height=0.06, wrapWidth=69.0, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    btn69_img_2 = visual.ImageStim(
        win=win,
        name='btn69_img_2', units='pix', 
        image='normal_next_btn.png', mask=None, anchor='center',
        ori=0.0, pos=(btm_x,btm_y), draggable=False, size=(btm_size_w,btm_size_h),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    mouse69_2 = event.Mouse(win=win)
    x, y = [None, None]
    mouse69_2.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "Review_trial" ---
    ans_rect = visual.Rect(
        win=win, name='ans_rect',units='height', 
        width=(1.3, 0.1)[0], height=(1.3, 0.1)[1],
        ori=0.0, pos=(-0.018, 0.048), draggable=False, anchor='center',
        lineWidth=10.0,
        colorSpace='rgb', lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, 1.0000, 1.0000],
        opacity=None, depth=0.0, interpolate=True)
    review_header = visual.TextStim(win=win, name='review_header',
        text='資訊說明複習',
        font='Noto Sans TC',
        units='height', pos=(0, 0.35), draggable=False, height=0.08, wrapWidth=69.0, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    ino_review_q = visual.TextStim(win=win, name='ino_review_q',
        text='替罪羔羊手法是如何誤導訊息的？\n\nA：把複雜問題全怪在同一個人或群體上，不談其他因素。\n\nB：列出多個可能成因並比較權重，不把問題刻意丟給單一方。',
        font='Noto Sans TC',
        units='height', pos=(0,0.05), draggable=False, height=0.05, wrapWidth=1.3, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    nonino_review_q = visual.TextStim(win=win, name='nonino_review_q',
        text='正確辨識海洋生物的方法是什麼？\n\nA：看外觀+棲地+習性，再對照圖鑑，多指標一致才判定。\n\nB：只看某一個特徵，之後再找資料確認',
        font='Noto Sans TC',
        units='height', pos=(0,0.05), draggable=False, height=0.05, wrapWidth=1.3, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    slider = visual.Slider(win=win, name='slider',
        startValue=None, size=(0.14, 0.05), pos=(-0.72, -0.025), units='height',
        labels=[2,1],ticks=None, granularity=1,
        style='radio', styleTweaks=(), opacity=None,
        labelColor=[1.0000, 1.0000, 1.0000], markerColor='Red', lineColor=[-0.0039, 1.0000, 0.6627], colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=90.0, depth=-4, readOnly=False)
    ansTag = visual.ShapeStim(
        win=win, name='ansTag',units='height', 
        size=(0.042), vertices='circle',
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=12.0,
        colorSpace='rgb', lineColor=[0.6549, 0.6549, 0.6549], fillColor=[1.0000, -1.0000, -1.0000],
        opacity=None, depth=-5.0, interpolate=True)
    noAnsTag = visual.ShapeStim(
        win=win, name='noAnsTag',units='height', 
        size=(0.042), vertices='circle',
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=12.0,
        colorSpace='rgb', lineColor=[0.6549, 0.6549, 0.6549], fillColor=[0.6549, 0.6549, 0.6549],
        opacity=None, depth=-6.0, interpolate=True)
    # Run 'Begin Experiment' code from code_2
    ino_review_q.alignText = 'left'
    nonino_review_q.alignText = 'left'
    ino_answer = visual.TextStim(win=win, name='ino_answer',
        text='答案：A（代罪羔羊的核心手法就是把複雜問題簡化成單一指責）',
        font='Noto Sans TC',
        units='height', pos=(0, -0.25), draggable=False, height=0.05, wrapWidth=2.0, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    nonino_answer = visual.TextStim(win=win, name='nonino_answer',
        text='答案：A（正確辨識的核心手法就是用多面向觀察反覆驗證）',
        font='Noto Sans TC',
        units='height', pos=(0, -0.25), draggable=False, height=0.05, wrapWidth=2.0, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-9.0);
    btn_rev_img = visual.ImageStim(
        win=win,
        name='btn_rev_img', units='pix', 
        image='normal_next_btn.png', mask=None, anchor='center',
        ori=0.0, pos=(btm_x,btm_y), draggable=False, size=(btm_size_w,btm_size_h),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-10.0)
    mouse_rev = event.Mouse(win=win)
    x, y = [None, None]
    mouse_rev.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "Start_Of_Practice" ---
    text_norm_2 = visual.TextStim(win=win, name='text_norm_2',
        text='本環節將會提供一篇貼文和隨機次序出現的三個問題進行作答\n\n每道題目需進行填答才會有「繼續」鍵的出現\n\n閱覽或作答完畢時請按「繼續」鍵',
        font='Noto Sans TC',
        units='pix', pos=(0, 0), draggable=False, height=50 * (screenX/screenY/form_related_ratio), wrapWidth=300000.0, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    btn6_img = visual.ImageStim(
        win=win,
        name='btn6_img', units='pix', 
        image='normal_next_btn.png', mask=None, anchor='center',
        ori=0.0, pos=(btm_x,btm_y), draggable=False, size=(btm_size_w,btm_size_h),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    mouse6 = event.Mouse(win=win)
    x, y = [None, None]
    mouse6.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "prepare_stim" ---
    
    # --- Initialize components for Routine "stimuli_img" ---
    stim_img = visual.ImageStim(
        win=win,
        name='stim_img', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    btn7_img = visual.ImageStim(
        win=win,
        name='btn7_img', units='pix', 
        image='normal_next_btn.png', mask=None, anchor='center',
        ori=0.0, pos=(btm_x,btm_y), draggable=False, size=(btm_size_w,btm_size_h),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    mouse7 = event.Mouse(win=win)
    x, y = [None, None]
    mouse7.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "resp_mixed" ---
    we_banner = visual.TextStim(win=win, name='we_banner',
        text='這篇貼文的哪個表情符號有最多回應？',
        font='Noto Sans TC',
        units='pix', pos=(0, resp_banner_y), draggable=False, height=resp_banner_h * (screenX/screenY/form_related_ratio), wrapWidth=69000.0, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    tof_banner = visual.TextStim(win=win, name='tof_banner',
        text='依據你對「資訊說明」的理解請判斷這則貼文的敘述方式',
        font='Noto Sans TC',
        units='pix', pos=(0, resp_banner_y), draggable=False, height=resp_banner_h * (screenX/screenY/form_related_ratio), wrapWidth=69000.0, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    att_banner = visual.TextStim(win=win, name='att_banner',
        text='你對此貼文抱持的態度？',
        font='Noto Sans TC',
        units='pix', pos=(0, resp_banner_y), draggable=False, height=resp_banner_h * (screenX/screenY/form_related_ratio), wrapWidth=69000.0, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    true_or_false = visual.Slider(win=win, name='true_or_false',
        startValue=5, size=(dv_wshort, dv_h), pos=(dv_x, dv_yshort), units='pix',
        labels=["完全無偏頗\n(0分)","1","2","3","4","有點偏頗\n(5分)","6","7","8","9","極度偏頗\n(10分)"], ticks=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=0.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor=[-1.0000, -1.0000, -1.0000], markerColor=[-1.0000, -1.0000, -1.0000], lineColor=[0.6314, 0.6549, 0.6000], colorSpace='rgb',
        font='Noto Sans TC', labelHeight=30 * (screenX/screenY/form_related_ratio),
        flip=False, ori=0.0, depth=-3, readOnly=False)
    tof_indicator = visual.TextStim(win=win, name='tof_indicator',
        text='',
        font='Noto Sans TC',
        units='norm', pos=(0.8, 0.6), draggable=False, height=0.087, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    pre_indicator = visual.TextStim(win=win, name='pre_indicator',
        text='',
        font='Noto Sans TC',
        units='norm', pos=(0.8, 0.6), draggable=False, height=0.087, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    which_emoji = visual.Slider(win=win, name='which_emoji',
        startValue=None, size=(dv_wlong, dv_h), pos=(dv_x, dv_ylong), units='pix',
        labels=["0","1","2","3","4","5","6"],ticks=None, granularity=1,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='white', markerColor='black', lineColor='LightGray', colorSpace='rgb',
        font='Noto Sans TC', labelHeight=45 * (screenX/screenY/form_related_ratio),
        flip=False, ori=0.0, depth=-6, readOnly=False)
    attitude_bg = visual.ImageStim(
        win=win,
        name='attitude_bg', units='pix', 
        image='path3.png', mask=None, anchor='center',
        ori=0.0, pos=(0, att_bg_y), draggable=False, size=(att_bg_w, att_bg_h),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    attitude = visual.Slider(win=win, name='attitude',
        startValue=5, size=(dv_wlong, dv_h), pos=(dv_x, dv_ylong), units='pix',
        labels=None, ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=0.0,
        style='rating', styleTweaks=(), opacity=0.0,
        labelColor=[-1.0000, -1.0000, -1.0000], markerColor=[-1.0000, -1.0000, -1.0000], lineColor=[0.6549, 0.6549, 0.6549], colorSpace='rgb',
        font='Noto Sans TC', labelHeight=45 * (screenX/screenY/form_related_ratio),
        flip=False, ori=0.0, depth=-8, readOnly=False)
    btn8_img = visual.ImageStim(
        win=win,
        name='btn8_img', units='pix', 
        image='normal_next_btn.png', mask=None, anchor='center',
        ori=0.0, pos=(btm_x,btm_y), draggable=False, size=(btm_size_w,btm_size_h),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-10.0)
    mouse8 = event.Mouse(win=win)
    x, y = [None, None]
    mouse8.mouseClock = core.Clock()
    we_bg = visual.ImageStim(
        win=win,
        name='we_bg', units='pix', 
        image='emoticon_all.png', mask=None, anchor='center',
        ori=0.0, pos=(0, we_bg_y), draggable=False, size=(we_bg_w, we_bg_h),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-13.0)
    stim_thumbnail = visual.ImageStim(
        win=win,
        name='stim_thumbnail', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-14.0)
    
    # --- Initialize components for Routine "End_Of_Practice" ---
    text_norm_3 = visual.TextStim(win=win, name='text_norm_3',
        text='即將進入正式題\n\n正式題與練習題模式一樣\n\n請用同樣方式作答',
        font='Noto Sans TC',
        units='pix', pos=(0, 0), draggable=False, height=50 * (screenX/screenY/form_related_ratio), wrapWidth=600000.0, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    btn9_img = visual.ImageStim(
        win=win,
        name='btn9_img', 
        image='normal_next_btn.png', mask=None, anchor='center',
        ori=0.0, pos=(btm_x,btm_y), draggable=False, size=(btm_size_w,btm_size_h),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    mouse9 = event.Mouse(win=win)
    x, y = [None, None]
    mouse9.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "prepare_stim" ---
    
    # --- Initialize components for Routine "stimuli_img" ---
    stim_img = visual.ImageStim(
        win=win,
        name='stim_img', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    btn7_img = visual.ImageStim(
        win=win,
        name='btn7_img', units='pix', 
        image='normal_next_btn.png', mask=None, anchor='center',
        ori=0.0, pos=(btm_x,btm_y), draggable=False, size=(btm_size_w,btm_size_h),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    mouse7 = event.Mouse(win=win)
    x, y = [None, None]
    mouse7.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "prepare_resp_order" ---
    
    # --- Initialize components for Routine "resp_mixed" ---
    we_banner = visual.TextStim(win=win, name='we_banner',
        text='這篇貼文的哪個表情符號有最多回應？',
        font='Noto Sans TC',
        units='pix', pos=(0, resp_banner_y), draggable=False, height=resp_banner_h * (screenX/screenY/form_related_ratio), wrapWidth=69000.0, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    tof_banner = visual.TextStim(win=win, name='tof_banner',
        text='依據你對「資訊說明」的理解請判斷這則貼文的敘述方式',
        font='Noto Sans TC',
        units='pix', pos=(0, resp_banner_y), draggable=False, height=resp_banner_h * (screenX/screenY/form_related_ratio), wrapWidth=69000.0, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    att_banner = visual.TextStim(win=win, name='att_banner',
        text='你對此貼文抱持的態度？',
        font='Noto Sans TC',
        units='pix', pos=(0, resp_banner_y), draggable=False, height=resp_banner_h * (screenX/screenY/form_related_ratio), wrapWidth=69000.0, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    true_or_false = visual.Slider(win=win, name='true_or_false',
        startValue=5, size=(dv_wshort, dv_h), pos=(dv_x, dv_yshort), units='pix',
        labels=["完全無偏頗\n(0分)","1","2","3","4","有點偏頗\n(5分)","6","7","8","9","極度偏頗\n(10分)"], ticks=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=0.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor=[-1.0000, -1.0000, -1.0000], markerColor=[-1.0000, -1.0000, -1.0000], lineColor=[0.6314, 0.6549, 0.6000], colorSpace='rgb',
        font='Noto Sans TC', labelHeight=30 * (screenX/screenY/form_related_ratio),
        flip=False, ori=0.0, depth=-3, readOnly=False)
    tof_indicator = visual.TextStim(win=win, name='tof_indicator',
        text='',
        font='Noto Sans TC',
        units='norm', pos=(0.8, 0.6), draggable=False, height=0.087, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    pre_indicator = visual.TextStim(win=win, name='pre_indicator',
        text='',
        font='Noto Sans TC',
        units='norm', pos=(0.8, 0.6), draggable=False, height=0.087, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    which_emoji = visual.Slider(win=win, name='which_emoji',
        startValue=None, size=(dv_wlong, dv_h), pos=(dv_x, dv_ylong), units='pix',
        labels=["0","1","2","3","4","5","6"],ticks=None, granularity=1,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='white', markerColor='black', lineColor='LightGray', colorSpace='rgb',
        font='Noto Sans TC', labelHeight=45 * (screenX/screenY/form_related_ratio),
        flip=False, ori=0.0, depth=-6, readOnly=False)
    attitude_bg = visual.ImageStim(
        win=win,
        name='attitude_bg', units='pix', 
        image='path3.png', mask=None, anchor='center',
        ori=0.0, pos=(0, att_bg_y), draggable=False, size=(att_bg_w, att_bg_h),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    attitude = visual.Slider(win=win, name='attitude',
        startValue=5, size=(dv_wlong, dv_h), pos=(dv_x, dv_ylong), units='pix',
        labels=None, ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=0.0,
        style='rating', styleTweaks=(), opacity=0.0,
        labelColor=[-1.0000, -1.0000, -1.0000], markerColor=[-1.0000, -1.0000, -1.0000], lineColor=[0.6549, 0.6549, 0.6549], colorSpace='rgb',
        font='Noto Sans TC', labelHeight=45 * (screenX/screenY/form_related_ratio),
        flip=False, ori=0.0, depth=-8, readOnly=False)
    btn8_img = visual.ImageStim(
        win=win,
        name='btn8_img', units='pix', 
        image='normal_next_btn.png', mask=None, anchor='center',
        ori=0.0, pos=(btm_x,btm_y), draggable=False, size=(btm_size_w,btm_size_h),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-10.0)
    mouse8 = event.Mouse(win=win)
    x, y = [None, None]
    mouse8.mouseClock = core.Clock()
    we_bg = visual.ImageStim(
        win=win,
        name='we_bg', units='pix', 
        image='emoticon_all.png', mask=None, anchor='center',
        ori=0.0, pos=(0, we_bg_y), draggable=False, size=(we_bg_w, we_bg_h),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-13.0)
    stim_thumbnail = visual.ImageStim(
        win=win,
        name='stim_thumbnail', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-14.0)
    
    # --- Initialize components for Routine "End_Of_Main_Trial" ---
    text_norm_4 = visual.TextStim(win=win, name='text_norm_4',
        text='實驗環節已結束\n\n麻煩請填寫事後問卷',
        font='Noto Sans TC',
        units='pix', pos=(0, 0), draggable=False, height=50 * (screenX/screenY/form_related_ratio), wrapWidth=60000.0, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    btn10_img = visual.ImageStim(
        win=win,
        name='btn10_img', 
        image='normal_next_btn.png', mask=None, anchor='center',
        ori=0.0, pos=(btm_x,btm_y), draggable=False, size=(btm_size_w,btm_size_h),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    mouse10 = event.Mouse(win=win)
    x, y = [None, None]
    mouse10.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "Political_Prefs_Form" ---
    win.allowStencil = True
    PBF_form = visual.Form(win=win, name='PBF_form',
        items='political_bias_form.csv',
        textHeight=0.03,
        font='Noto Sans TC',
        randomize=False,
        style='custom...',
        fillColor=[1.0000, 1.0000, 1.0000], borderColor=[-1.0000, -1.0000, -1.0000], itemColor='black', 
        responseColor='black', markerColor='black', colorSpace='rgb', 
        size=(form_wHeight,form_hHeight),
        pos=(form_xHeight,form_yHeight),
        itemPadding=0.1,
        depth=0
    )
    btn3_img = visual.ImageStim(
        win=win,
        name='btn3_img', units='pix', 
        image='normal_next_btn.png', mask=None, anchor='center',
        ori=0.0, pos=(btm_x,btm_y), draggable=False, size=(btm_size_w,btm_size_h),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    mouse3 = event.Mouse(win=win)
    x, y = [None, None]
    mouse3.mouseClock = core.Clock()
    pre_indicator_2 = visual.TextStim(win=win, name='pre_indicator_2',
        text='[請填寫表單]',
        font='Noto Sans TC',
        units='height', pos=((-0.02 + btm_x/screenX) * (screenX/screenY), btm_y/screenY), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "End_Of_Experiment" ---
    goodbye_text = visual.TextStim(win=win, name='goodbye_text',
        text='實驗結束，感謝參與本實驗。',
        font='Noto Sans TC',
        units='norm', pos=(0, 0), draggable=False, height=0.092, wrapWidth=1.8, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
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
    
    # --- Prepare to start Routine "prepare_everything" ---
    # create an object to store info about Routine prepare_everything
    prepare_everything = data.Routine(
        name='prepare_everything',
        components=[],
    )
    prepare_everything.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from prepare_code
    text_norm69.alignText= 'center'
    
    # store start times for prepare_everything
    prepare_everything.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    prepare_everything.tStart = globalClock.getTime(format='float')
    prepare_everything.status = STARTED
    thisExp.addData('prepare_everything.started', prepare_everything.tStart)
    prepare_everything.maxDuration = None
    # keep track of which components have finished
    prepare_everythingComponents = prepare_everything.components
    for thisComponent in prepare_everything.components:
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
    
    # --- Run Routine "prepare_everything" ---
    prepare_everything.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
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
                currentRoutine=prepare_everything,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            prepare_everything.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prepare_everything.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prepare_everything" ---
    for thisComponent in prepare_everything.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for prepare_everything
    prepare_everything.tStop = globalClock.getTime(format='float')
    prepare_everything.tStopRefresh = tThisFlipGlobal
    thisExp.addData('prepare_everything.stopped', prepare_everything.tStop)
    thisExp.nextEntry()
    # the Routine "prepare_everything" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Introduction" ---
    # create an object to store info about Routine Introduction
    Introduction = data.Routine(
        name='Introduction',
        components=[text_norm69, btn1_img, mouse1],
    )
    Introduction.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse1
    mouse1.x = []
    mouse1.y = []
    mouse1.leftButton = []
    mouse1.midButton = []
    mouse1.rightButton = []
    mouse1.time = []
    mouse1.clicked_name = []
    gotValidClick = False  # until a click is received
    # store start times for Introduction
    Introduction.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Introduction.tStart = globalClock.getTime(format='float')
    Introduction.status = STARTED
    thisExp.addData('Introduction.started', Introduction.tStart)
    Introduction.maxDuration = None
    # keep track of which components have finished
    IntroductionComponents = Introduction.components
    for thisComponent in Introduction.components:
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
    
    # --- Run Routine "Introduction" ---
    Introduction.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_norm69* updates
        
        # if text_norm69 is starting this frame...
        if text_norm69.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_norm69.frameNStart = frameN  # exact frame index
            text_norm69.tStart = t  # local t and not account for scr refresh
            text_norm69.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_norm69, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_norm69.status = STARTED
            text_norm69.setAutoDraw(True)
        
        # if text_norm69 is active this frame...
        if text_norm69.status == STARTED:
            # update params
            pass
        
        # *btn1_img* updates
        
        # if btn1_img is starting this frame...
        if btn1_img.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            btn1_img.frameNStart = frameN  # exact frame index
            btn1_img.tStart = t  # local t and not account for scr refresh
            btn1_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(btn1_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'btn1_img.started')
            # update status
            btn1_img.status = STARTED
            btn1_img.setAutoDraw(True)
        
        # if btn1_img is active this frame...
        if btn1_img.status == STARTED:
            # update params
            pass
        # Run 'Each Frame' code from btn1_color_code
        # 滑鼠位置
        mouseX, mouseY = mouse1.getPos()
        
        # 圖片邊界
        btn_left = btn1_img.pos[0] - btn1_img.size[0]/2
        btn_right = btn1_img.pos[0] + btn1_img.size[0]/2
        btn_top = btn1_img.pos[1] + btn1_img.size[1]/2
        btn_bottom = btn1_img.pos[1] - btn1_img.size[1]/2
        
        # 檢查滑鼠是否在圖片上
        if btn_left <= mouseX <= btn_right and btn_bottom <= mouseY <= btn_top:
            btn1_img.image = 'highlight_next_btn.png'  # 滑鼠移到上面時，換成高亮圖片
        else:
            btn1_img.image = 'normal_next_btn.png'     # 滑鼠移開時，換回原圖
        
        # *mouse1* updates
        
        # if mouse1 is starting this frame...
        if mouse1.status == NOT_STARTED and t >= mouse_debounce_timeout-frameTolerance:
            # keep track of start time/frame for later
            mouse1.frameNStart = frameN  # exact frame index
            mouse1.tStart = t  # local t and not account for scr refresh
            mouse1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse1.started', t)
            # update status
            mouse1.status = STARTED
            mouse1.mouseClock.reset()
            prevButtonState = mouse1.getPressed()  # if button is down already this ISN'T a new click
        if mouse1.status == STARTED:  # only update if started and not finished!
            buttons = mouse1.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(btn1_img, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse1):
                            gotValidClick = True
                            mouse1.clicked_name.append(obj.name)
                    if not gotValidClick:
                        mouse1.clicked_name.append(None)
                    x, y = mouse1.getPos()
                    mouse1.x.append(x)
                    mouse1.y.append(y)
                    buttons = mouse1.getPressed()
                    mouse1.leftButton.append(buttons[0])
                    mouse1.midButton.append(buttons[1])
                    mouse1.rightButton.append(buttons[2])
                    mouse1.time.append(mouse1.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
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
                currentRoutine=Introduction,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Introduction.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Introduction.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Introduction" ---
    for thisComponent in Introduction.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Introduction
    Introduction.tStop = globalClock.getTime(format='float')
    Introduction.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Introduction.stopped', Introduction.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse1.x', mouse1.x)
    thisExp.addData('mouse1.y', mouse1.y)
    thisExp.addData('mouse1.leftButton', mouse1.leftButton)
    thisExp.addData('mouse1.midButton', mouse1.midButton)
    thisExp.addData('mouse1.rightButton', mouse1.rightButton)
    thisExp.addData('mouse1.time', mouse1.time)
    thisExp.addData('mouse1.clicked_name', mouse1.clicked_name)
    thisExp.nextEntry()
    # the Routine "Introduction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Demographic_Form" ---
    # create an object to store info about Routine Demographic_Form
    Demographic_Form = data.Routine(
        name='Demographic_Form',
        components=[demog_form, btn2_img, mouse2, pre_indicator_3],
    )
    Demographic_Form.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse2
    mouse2.x = []
    mouse2.y = []
    mouse2.leftButton = []
    mouse2.midButton = []
    mouse2.rightButton = []
    mouse2.time = []
    mouse2.clicked_name = []
    gotValidClick = False  # until a click is received
    # store start times for Demographic_Form
    Demographic_Form.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Demographic_Form.tStart = globalClock.getTime(format='float')
    Demographic_Form.status = STARTED
    thisExp.addData('Demographic_Form.started', Demographic_Form.tStart)
    Demographic_Form.maxDuration = None
    # keep track of which components have finished
    Demographic_FormComponents = Demographic_Form.components
    for thisComponent in Demographic_Form.components:
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
    
    # --- Run Routine "Demographic_Form" ---
    Demographic_Form.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *demog_form* updates
        
        # if demog_form is starting this frame...
        if demog_form.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            demog_form.frameNStart = frameN  # exact frame index
            demog_form.tStart = t  # local t and not account for scr refresh
            demog_form.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(demog_form, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'demog_form.started')
            # update status
            demog_form.status = STARTED
            demog_form.setAutoDraw(True)
        
        # if demog_form is active this frame...
        if demog_form.status == STARTED:
            # update params
            pass
        
        # *btn2_img* updates
        
        # if btn2_img is starting this frame...
        if btn2_img.status == NOT_STARTED and demog_form.complete:
            # keep track of start time/frame for later
            btn2_img.frameNStart = frameN  # exact frame index
            btn2_img.tStart = t  # local t and not account for scr refresh
            btn2_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(btn2_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'btn2_img.started')
            # update status
            btn2_img.status = STARTED
            btn2_img.setAutoDraw(True)
        
        # if btn2_img is active this frame...
        if btn2_img.status == STARTED:
            # update params
            pass
        # Run 'Each Frame' code from btn2_color_code
        # 滑鼠位置
        mouseX, mouseY = mouse2.getPos()
        
        # 圖片邊界
        btn_left = btn2_img.pos[0] - btn2_img.size[0]/2
        btn_right = btn2_img.pos[0] + btn2_img.size[0]/2
        btn_top = btn2_img.pos[1] + btn2_img.size[1]/2
        btn_bottom = btn2_img.pos[1] - btn2_img.size[1]/2
        
        # 檢查滑鼠是否在圖片上
        if btn_left <= mouseX <= btn_right and btn_bottom <= mouseY <= btn_top:
            btn2_img.image = 'highlight_next_btn.png'  # 滑鼠移到上面時，換成高亮圖片
        else:
            btn2_img.image = 'normal_next_btn.png'     # 滑鼠移開時，換回原圖
        
        # *mouse2* updates
        
        # if mouse2 is starting this frame...
        if mouse2.status == NOT_STARTED and demog_form.complete:
            # keep track of start time/frame for later
            mouse2.frameNStart = frameN  # exact frame index
            mouse2.tStart = t  # local t and not account for scr refresh
            mouse2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse2.started', t)
            # update status
            mouse2.status = STARTED
            mouse2.mouseClock.reset()
            prevButtonState = mouse2.getPressed()  # if button is down already this ISN'T a new click
        if mouse2.status == STARTED:  # only update if started and not finished!
            buttons = mouse2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(btn2_img, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse2):
                            gotValidClick = True
                            mouse2.clicked_name.append(obj.name)
                    if not gotValidClick:
                        mouse2.clicked_name.append(None)
                    x, y = mouse2.getPos()
                    mouse2.x.append(x)
                    mouse2.y.append(y)
                    buttons = mouse2.getPressed()
                    mouse2.leftButton.append(buttons[0])
                    mouse2.midButton.append(buttons[1])
                    mouse2.rightButton.append(buttons[2])
                    mouse2.time.append(mouse2.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # *pre_indicator_3* updates
        
        # if pre_indicator_3 is starting this frame...
        if pre_indicator_3.status == NOT_STARTED and not demog_form.complete:
            # keep track of start time/frame for later
            pre_indicator_3.frameNStart = frameN  # exact frame index
            pre_indicator_3.tStart = t  # local t and not account for scr refresh
            pre_indicator_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pre_indicator_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pre_indicator_3.started')
            # update status
            pre_indicator_3.status = STARTED
            pre_indicator_3.setAutoDraw(True)
        
        # if pre_indicator_3 is active this frame...
        if pre_indicator_3.status == STARTED:
            # update params
            pass
        
        # if pre_indicator_3 is stopping this frame...
        if pre_indicator_3.status == STARTED:
            if bool(demog_form.complete):
                # keep track of stop time/frame for later
                pre_indicator_3.tStop = t  # not accounting for scr refresh
                pre_indicator_3.tStopRefresh = tThisFlipGlobal  # on global time
                pre_indicator_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pre_indicator_3.stopped')
                # update status
                pre_indicator_3.status = FINISHED
                pre_indicator_3.setAutoDraw(False)
        
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
                currentRoutine=Demographic_Form,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Demographic_Form.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Demographic_Form.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Demographic_Form" ---
    for thisComponent in Demographic_Form.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Demographic_Form
    Demographic_Form.tStop = globalClock.getTime(format='float')
    Demographic_Form.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Demographic_Form.stopped', Demographic_Form.tStop)
    demog_form.addDataToExp(thisExp, 'rows')
    demog_form.autodraw = False
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse2.x', mouse2.x)
    thisExp.addData('mouse2.y', mouse2.y)
    thisExp.addData('mouse2.leftButton', mouse2.leftButton)
    thisExp.addData('mouse2.midButton', mouse2.midButton)
    thisExp.addData('mouse2.rightButton', mouse2.rightButton)
    thisExp.addData('mouse2.time', mouse2.time)
    thisExp.addData('mouse2.clicked_name', mouse2.clicked_name)
    thisExp.nextEntry()
    # the Routine "Demographic_Form" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Ino_Intro" ---
    # create an object to store info about Routine Ino_Intro
    Ino_Intro = data.Routine(
        name='Ino_Intro',
        components=[text_norm_6, btn69_img, mouse69],
    )
    Ino_Intro.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse69
    mouse69.x = []
    mouse69.y = []
    mouse69.leftButton = []
    mouse69.midButton = []
    mouse69.rightButton = []
    mouse69.time = []
    mouse69.clicked_name = []
    gotValidClick = False  # until a click is received
    # store start times for Ino_Intro
    Ino_Intro.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Ino_Intro.tStart = globalClock.getTime(format='float')
    Ino_Intro.status = STARTED
    thisExp.addData('Ino_Intro.started', Ino_Intro.tStart)
    Ino_Intro.maxDuration = None
    # keep track of which components have finished
    Ino_IntroComponents = Ino_Intro.components
    for thisComponent in Ino_Intro.components:
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
    
    # --- Run Routine "Ino_Intro" ---
    Ino_Intro.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_norm_6* updates
        
        # if text_norm_6 is starting this frame...
        if text_norm_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_norm_6.frameNStart = frameN  # exact frame index
            text_norm_6.tStart = t  # local t and not account for scr refresh
            text_norm_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_norm_6, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_norm_6.status = STARTED
            text_norm_6.setAutoDraw(True)
        
        # if text_norm_6 is active this frame...
        if text_norm_6.status == STARTED:
            # update params
            pass
        
        # *btn69_img* updates
        
        # if btn69_img is starting this frame...
        if btn69_img.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            btn69_img.frameNStart = frameN  # exact frame index
            btn69_img.tStart = t  # local t and not account for scr refresh
            btn69_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(btn69_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'btn69_img.started')
            # update status
            btn69_img.status = STARTED
            btn69_img.setAutoDraw(True)
        
        # if btn69_img is active this frame...
        if btn69_img.status == STARTED:
            # update params
            pass
        # Run 'Each Frame' code from btn69_color_code
        # 滑鼠位置
        mouseX, mouseY = mouse69.getPos()
        
        # 圖片邊界
        btn_left = btn69_img.pos[0] - btn69_img.size[0]/2
        btn_right = btn69_img.pos[0] + btn69_img.size[0]/2
        btn_top = btn69_img.pos[1] + btn69_img.size[1]/2
        btn_bottom = btn69_img.pos[1] - btn69_img.size[1]/2
        
        # 檢查滑鼠是否在圖片上
        if btn_left <= mouseX <= btn_right and btn_bottom <= mouseY <= btn_top:
            btn69_img.image = 'highlight_next_btn.png'  # 滑鼠移到上面時，換成高亮圖片
        else:
            btn69_img.image = 'normal_next_btn.png'     # 滑鼠移開時，換回原圖
        
        # *mouse69* updates
        
        # if mouse69 is starting this frame...
        if mouse69.status == NOT_STARTED and t >= mouse_debounce_timeout-frameTolerance:
            # keep track of start time/frame for later
            mouse69.frameNStart = frameN  # exact frame index
            mouse69.tStart = t  # local t and not account for scr refresh
            mouse69.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse69, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse69.started', t)
            # update status
            mouse69.status = STARTED
            mouse69.mouseClock.reset()
            prevButtonState = mouse69.getPressed()  # if button is down already this ISN'T a new click
        if mouse69.status == STARTED:  # only update if started and not finished!
            buttons = mouse69.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(btn69_img, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse69):
                            gotValidClick = True
                            mouse69.clicked_name.append(obj.name)
                    if not gotValidClick:
                        mouse69.clicked_name.append(None)
                    x, y = mouse69.getPos()
                    mouse69.x.append(x)
                    mouse69.y.append(y)
                    buttons = mouse69.getPressed()
                    mouse69.leftButton.append(buttons[0])
                    mouse69.midButton.append(buttons[1])
                    mouse69.rightButton.append(buttons[2])
                    mouse69.time.append(mouse69.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
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
                currentRoutine=Ino_Intro,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Ino_Intro.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Ino_Intro.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Ino_Intro" ---
    for thisComponent in Ino_Intro.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Ino_Intro
    Ino_Intro.tStop = globalClock.getTime(format='float')
    Ino_Intro.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Ino_Intro.stopped', Ino_Intro.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse69.x', mouse69.x)
    thisExp.addData('mouse69.y', mouse69.y)
    thisExp.addData('mouse69.leftButton', mouse69.leftButton)
    thisExp.addData('mouse69.midButton', mouse69.midButton)
    thisExp.addData('mouse69.rightButton', mouse69.rightButton)
    thisExp.addData('mouse69.time', mouse69.time)
    thisExp.addData('mouse69.clicked_name', mouse69.clicked_name)
    thisExp.nextEntry()
    # the Routine "Ino_Intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Inoculation" ---
    # create an object to store info about Routine Inoculation
    Inoculation = data.Routine(
        name='Inoculation',
        components=[btn4_img, mouse4, image],
    )
    Inoculation.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse4
    mouse4.x = []
    mouse4.y = []
    mouse4.leftButton = []
    mouse4.midButton = []
    mouse4.rightButton = []
    mouse4.time = []
    mouse4.clicked_name = []
    gotValidClick = False  # until a click is received
    # store start times for Inoculation
    Inoculation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Inoculation.tStart = globalClock.getTime(format='float')
    Inoculation.status = STARTED
    thisExp.addData('Inoculation.started', Inoculation.tStart)
    Inoculation.maxDuration = None
    # skip Routine Inoculation if its 'Skip if' condition is True
    Inoculation.skipped = continueRoutine and not (not inoculation_switch)
    continueRoutine = Inoculation.skipped
    # keep track of which components have finished
    InoculationComponents = Inoculation.components
    for thisComponent in Inoculation.components:
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
    
    # --- Run Routine "Inoculation" ---
    Inoculation.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *btn4_img* updates
        
        # if btn4_img is starting this frame...
        if btn4_img.status == NOT_STARTED and tThisFlip >= inoculation_debounce_timeout-frameTolerance:
            # keep track of start time/frame for later
            btn4_img.frameNStart = frameN  # exact frame index
            btn4_img.tStart = t  # local t and not account for scr refresh
            btn4_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(btn4_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'btn4_img.started')
            # update status
            btn4_img.status = STARTED
            btn4_img.setAutoDraw(True)
        
        # if btn4_img is active this frame...
        if btn4_img.status == STARTED:
            # update params
            pass
        # Run 'Each Frame' code from btn4_color_code
        # 滑鼠位置
        mouseX, mouseY = mouse4.getPos()
        
        # 圖片邊界
        btn_left = btn4_img.pos[0] - btn4_img.size[0]/2
        btn_right = btn4_img.pos[0] + btn4_img.size[0]/2
        btn_top = btn4_img.pos[1] + btn4_img.size[1]/2
        btn_bottom = btn4_img.pos[1] - btn4_img.size[1]/2
        
        # 檢查滑鼠是否在圖片上
        if btn_left <= mouseX <= btn_right and btn_bottom <= mouseY <= btn_top:
            btn4_img.image = 'highlight_next_btn.png'  # 滑鼠移到上面時，換成高亮圖片
        else:
            btn4_img.image = 'normal_next_btn.png'     # 滑鼠移開時，換回原圖
        
        # *mouse4* updates
        
        # if mouse4 is starting this frame...
        if mouse4.status == NOT_STARTED and t >= inoculation_debounce_timeout-frameTolerance:
            # keep track of start time/frame for later
            mouse4.frameNStart = frameN  # exact frame index
            mouse4.tStart = t  # local t and not account for scr refresh
            mouse4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse4.started', t)
            # update status
            mouse4.status = STARTED
            mouse4.mouseClock.reset()
            prevButtonState = mouse4.getPressed()  # if button is down already this ISN'T a new click
        if mouse4.status == STARTED:  # only update if started and not finished!
            buttons = mouse4.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(btn4_img, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse4):
                            gotValidClick = True
                            mouse4.clicked_name.append(obj.name)
                    if not gotValidClick:
                        mouse4.clicked_name.append(None)
                    x, y = mouse4.getPos()
                    mouse4.x.append(x)
                    mouse4.y.append(y)
                    buttons = mouse4.getPressed()
                    mouse4.leftButton.append(buttons[0])
                    mouse4.midButton.append(buttons[1])
                    mouse4.rightButton.append(buttons[2])
                    mouse4.time.append(mouse4.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # *image* updates
        
        # if image is starting this frame...
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image.started')
            # update status
            image.status = STARTED
            image.setAutoDraw(True)
        
        # if image is active this frame...
        if image.status == STARTED:
            # update params
            pass
        
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
                currentRoutine=Inoculation,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Inoculation.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Inoculation.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Inoculation" ---
    for thisComponent in Inoculation.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Inoculation
    Inoculation.tStop = globalClock.getTime(format='float')
    Inoculation.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Inoculation.stopped', Inoculation.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse4.x', mouse4.x)
    thisExp.addData('mouse4.y', mouse4.y)
    thisExp.addData('mouse4.leftButton', mouse4.leftButton)
    thisExp.addData('mouse4.midButton', mouse4.midButton)
    thisExp.addData('mouse4.rightButton', mouse4.rightButton)
    thisExp.addData('mouse4.time', mouse4.time)
    thisExp.addData('mouse4.clicked_name', mouse4.clicked_name)
    thisExp.nextEntry()
    # the Routine "Inoculation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "NonInoculation" ---
    # create an object to store info about Routine NonInoculation
    NonInoculation = data.Routine(
        name='NonInoculation',
        components=[btn5_img, mouse5, image_2],
    )
    NonInoculation.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse5
    mouse5.x = []
    mouse5.y = []
    mouse5.leftButton = []
    mouse5.midButton = []
    mouse5.rightButton = []
    mouse5.time = []
    mouse5.clicked_name = []
    gotValidClick = False  # until a click is received
    # store start times for NonInoculation
    NonInoculation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    NonInoculation.tStart = globalClock.getTime(format='float')
    NonInoculation.status = STARTED
    thisExp.addData('NonInoculation.started', NonInoculation.tStart)
    NonInoculation.maxDuration = None
    # skip Routine NonInoculation if its 'Skip if' condition is True
    NonInoculation.skipped = continueRoutine and not (inoculation_switch)
    continueRoutine = NonInoculation.skipped
    # keep track of which components have finished
    NonInoculationComponents = NonInoculation.components
    for thisComponent in NonInoculation.components:
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
    
    # --- Run Routine "NonInoculation" ---
    NonInoculation.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *btn5_img* updates
        
        # if btn5_img is starting this frame...
        if btn5_img.status == NOT_STARTED and tThisFlip >= inoculation_debounce_timeout-frameTolerance:
            # keep track of start time/frame for later
            btn5_img.frameNStart = frameN  # exact frame index
            btn5_img.tStart = t  # local t and not account for scr refresh
            btn5_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(btn5_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'btn5_img.started')
            # update status
            btn5_img.status = STARTED
            btn5_img.setAutoDraw(True)
        
        # if btn5_img is active this frame...
        if btn5_img.status == STARTED:
            # update params
            pass
        # Run 'Each Frame' code from btn5_color_code
        # 滑鼠位置
        mouseX, mouseY = mouse5.getPos()
        
        # 圖片邊界
        btn_left = btn5_img.pos[0] - btn5_img.size[0]/2
        btn_right = btn5_img.pos[0] + btn5_img.size[0]/2
        btn_top = btn5_img.pos[1] + btn5_img.size[1]/2
        btn_bottom = btn5_img.pos[1] - btn5_img.size[1]/2
        
        # 檢查滑鼠是否在圖片上
        if btn_left <= mouseX <= btn_right and btn_bottom <= mouseY <= btn_top:
            btn5_img.image = 'highlight_next_btn.png'  # 滑鼠移到上面時，換成高亮圖片
        else:
            btn5_img.image = 'normal_next_btn.png'     # 滑鼠移開時，換回原圖
        
        # *mouse5* updates
        
        # if mouse5 is starting this frame...
        if mouse5.status == NOT_STARTED and t >= inoculation_debounce_timeout-frameTolerance:
            # keep track of start time/frame for later
            mouse5.frameNStart = frameN  # exact frame index
            mouse5.tStart = t  # local t and not account for scr refresh
            mouse5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse5.started', t)
            # update status
            mouse5.status = STARTED
            mouse5.mouseClock.reset()
            prevButtonState = mouse5.getPressed()  # if button is down already this ISN'T a new click
        if mouse5.status == STARTED:  # only update if started and not finished!
            buttons = mouse5.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(btn5_img, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse5):
                            gotValidClick = True
                            mouse5.clicked_name.append(obj.name)
                    if not gotValidClick:
                        mouse5.clicked_name.append(None)
                    x, y = mouse5.getPos()
                    mouse5.x.append(x)
                    mouse5.y.append(y)
                    buttons = mouse5.getPressed()
                    mouse5.leftButton.append(buttons[0])
                    mouse5.midButton.append(buttons[1])
                    mouse5.rightButton.append(buttons[2])
                    mouse5.time.append(mouse5.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # *image_2* updates
        
        # if image_2 is starting this frame...
        if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_2.started')
            # update status
            image_2.status = STARTED
            image_2.setAutoDraw(True)
        
        # if image_2 is active this frame...
        if image_2.status == STARTED:
            # update params
            pass
        
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
                currentRoutine=NonInoculation,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            NonInoculation.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NonInoculation.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "NonInoculation" ---
    for thisComponent in NonInoculation.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for NonInoculation
    NonInoculation.tStop = globalClock.getTime(format='float')
    NonInoculation.tStopRefresh = tThisFlipGlobal
    thisExp.addData('NonInoculation.stopped', NonInoculation.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse5.x', mouse5.x)
    thisExp.addData('mouse5.y', mouse5.y)
    thisExp.addData('mouse5.leftButton', mouse5.leftButton)
    thisExp.addData('mouse5.midButton', mouse5.midButton)
    thisExp.addData('mouse5.rightButton', mouse5.rightButton)
    thisExp.addData('mouse5.time', mouse5.time)
    thisExp.addData('mouse5.clicked_name', mouse5.clicked_name)
    thisExp.nextEntry()
    # the Routine "NonInoculation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Review_Intro" ---
    # create an object to store info about Routine Review_Intro
    Review_Intro = data.Routine(
        name='Review_Intro',
        components=[text_norm_7, btn69_img_2, mouse69_2],
    )
    Review_Intro.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse69_2
    mouse69_2.x = []
    mouse69_2.y = []
    mouse69_2.leftButton = []
    mouse69_2.midButton = []
    mouse69_2.rightButton = []
    mouse69_2.time = []
    mouse69_2.clicked_name = []
    gotValidClick = False  # until a click is received
    # store start times for Review_Intro
    Review_Intro.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Review_Intro.tStart = globalClock.getTime(format='float')
    Review_Intro.status = STARTED
    thisExp.addData('Review_Intro.started', Review_Intro.tStart)
    Review_Intro.maxDuration = None
    # keep track of which components have finished
    Review_IntroComponents = Review_Intro.components
    for thisComponent in Review_Intro.components:
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
    
    # --- Run Routine "Review_Intro" ---
    Review_Intro.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_norm_7* updates
        
        # if text_norm_7 is starting this frame...
        if text_norm_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_norm_7.frameNStart = frameN  # exact frame index
            text_norm_7.tStart = t  # local t and not account for scr refresh
            text_norm_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_norm_7, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_norm_7.status = STARTED
            text_norm_7.setAutoDraw(True)
        
        # if text_norm_7 is active this frame...
        if text_norm_7.status == STARTED:
            # update params
            pass
        
        # *btn69_img_2* updates
        
        # if btn69_img_2 is starting this frame...
        if btn69_img_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            btn69_img_2.frameNStart = frameN  # exact frame index
            btn69_img_2.tStart = t  # local t and not account for scr refresh
            btn69_img_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(btn69_img_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'btn69_img_2.started')
            # update status
            btn69_img_2.status = STARTED
            btn69_img_2.setAutoDraw(True)
        
        # if btn69_img_2 is active this frame...
        if btn69_img_2.status == STARTED:
            # update params
            pass
        # Run 'Each Frame' code from btn69_color_code_2
        # 滑鼠位置
        mouseX, mouseY = mouse69_2.getPos()
        
        # 圖片邊界
        btn_left = btn69_img_2.pos[0] - btn69_img_2.size[0]/2
        btn_right = btn69_img.pos[0] + btn69_img_2.size[0]/2
        btn_top = btn69_img_2.pos[1] + btn69_img_2.size[1]/2
        btn_bottom = btn69_img_2.pos[1] - btn69_img_2.size[1]/2
        
        # 檢查滑鼠是否在圖片上
        if btn_left <= mouseX <= btn_right and btn_bottom <= mouseY <= btn_top:
            btn69_img_2.image = 'highlight_next_btn.png'  # 滑鼠移到上面時，換成高亮圖片
        else:
            btn69_img_2.image = 'normal_next_btn.png'     # 滑鼠移開時，換回原圖
        
        # *mouse69_2* updates
        
        # if mouse69_2 is starting this frame...
        if mouse69_2.status == NOT_STARTED and t >= mouse_debounce_timeout-frameTolerance:
            # keep track of start time/frame for later
            mouse69_2.frameNStart = frameN  # exact frame index
            mouse69_2.tStart = t  # local t and not account for scr refresh
            mouse69_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse69_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse69_2.started', t)
            # update status
            mouse69_2.status = STARTED
            mouse69_2.mouseClock.reset()
            prevButtonState = mouse69_2.getPressed()  # if button is down already this ISN'T a new click
        if mouse69_2.status == STARTED:  # only update if started and not finished!
            buttons = mouse69_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(btn69_img_2, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse69_2):
                            gotValidClick = True
                            mouse69_2.clicked_name.append(obj.name)
                    if not gotValidClick:
                        mouse69_2.clicked_name.append(None)
                    x, y = mouse69_2.getPos()
                    mouse69_2.x.append(x)
                    mouse69_2.y.append(y)
                    buttons = mouse69_2.getPressed()
                    mouse69_2.leftButton.append(buttons[0])
                    mouse69_2.midButton.append(buttons[1])
                    mouse69_2.rightButton.append(buttons[2])
                    mouse69_2.time.append(mouse69_2.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
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
                currentRoutine=Review_Intro,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Review_Intro.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Review_Intro.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Review_Intro" ---
    for thisComponent in Review_Intro.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Review_Intro
    Review_Intro.tStop = globalClock.getTime(format='float')
    Review_Intro.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Review_Intro.stopped', Review_Intro.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse69_2.x', mouse69_2.x)
    thisExp.addData('mouse69_2.y', mouse69_2.y)
    thisExp.addData('mouse69_2.leftButton', mouse69_2.leftButton)
    thisExp.addData('mouse69_2.midButton', mouse69_2.midButton)
    thisExp.addData('mouse69_2.rightButton', mouse69_2.rightButton)
    thisExp.addData('mouse69_2.time', mouse69_2.time)
    thisExp.addData('mouse69_2.clicked_name', mouse69_2.clicked_name)
    thisExp.nextEntry()
    # the Routine "Review_Intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Review_trial" ---
    # create an object to store info about Routine Review_trial
    Review_trial = data.Routine(
        name='Review_trial',
        components=[ans_rect, review_header, ino_review_q, nonino_review_q, slider, ansTag, noAnsTag, ino_answer, nonino_answer, btn_rev_img, mouse_rev],
    )
    Review_trial.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    slider.reset()
    # Run 'Begin Routine' code from code_2
    slider_placeholder = 0
    selection_time = None
    next_button_enable = 0
    
    #Review part
    upper_ansYH = 0.045
    lower_ansTH = -0.095
    AnsY = 0
    NoAnsY = 0
    # setup some python lists for storing info about the mouse_rev
    mouse_rev.x = []
    mouse_rev.y = []
    mouse_rev.leftButton = []
    mouse_rev.midButton = []
    mouse_rev.rightButton = []
    mouse_rev.time = []
    mouse_rev.clicked_name = []
    gotValidClick = False  # until a click is received
    # store start times for Review_trial
    Review_trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Review_trial.tStart = globalClock.getTime(format='float')
    Review_trial.status = STARTED
    thisExp.addData('Review_trial.started', Review_trial.tStart)
    Review_trial.maxDuration = None
    # keep track of which components have finished
    Review_trialComponents = Review_trial.components
    for thisComponent in Review_trial.components:
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
    
    # --- Run Routine "Review_trial" ---
    Review_trial.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ans_rect* updates
        
        # if ans_rect is starting this frame...
        if ans_rect.status == NOT_STARTED and slider_placeholder == 1:
            # keep track of start time/frame for later
            ans_rect.frameNStart = frameN  # exact frame index
            ans_rect.tStart = t  # local t and not account for scr refresh
            ans_rect.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans_rect, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ans_rect.started')
            # update status
            ans_rect.status = STARTED
            ans_rect.setAutoDraw(True)
        
        # if ans_rect is active this frame...
        if ans_rect.status == STARTED:
            # update params
            pass
        
        # *review_header* updates
        
        # if review_header is starting this frame...
        if review_header.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            review_header.frameNStart = frameN  # exact frame index
            review_header.tStart = t  # local t and not account for scr refresh
            review_header.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(review_header, 'tStartRefresh')  # time at next scr refresh
            # update status
            review_header.status = STARTED
            review_header.setAutoDraw(True)
        
        # if review_header is active this frame...
        if review_header.status == STARTED:
            # update params
            pass
        
        # *ino_review_q* updates
        
        # if ino_review_q is starting this frame...
        if ino_review_q.status == NOT_STARTED and inoculation_switch == 1:
            # keep track of start time/frame for later
            ino_review_q.frameNStart = frameN  # exact frame index
            ino_review_q.tStart = t  # local t and not account for scr refresh
            ino_review_q.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ino_review_q, 'tStartRefresh')  # time at next scr refresh
            # update status
            ino_review_q.status = STARTED
            ino_review_q.setAutoDraw(True)
        
        # if ino_review_q is active this frame...
        if ino_review_q.status == STARTED:
            # update params
            pass
        
        # *nonino_review_q* updates
        
        # if nonino_review_q is starting this frame...
        if nonino_review_q.status == NOT_STARTED and inoculation_switch == 0:
            # keep track of start time/frame for later
            nonino_review_q.frameNStart = frameN  # exact frame index
            nonino_review_q.tStart = t  # local t and not account for scr refresh
            nonino_review_q.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nonino_review_q, 'tStartRefresh')  # time at next scr refresh
            # update status
            nonino_review_q.status = STARTED
            nonino_review_q.setAutoDraw(True)
        
        # if nonino_review_q is active this frame...
        if nonino_review_q.status == STARTED:
            # update params
            pass
        
        # *slider* updates
        
        # if slider is starting this frame...
        if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider.frameNStart = frameN  # exact frame index
            slider.tStart = t  # local t and not account for scr refresh
            slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider.started')
            # update status
            slider.status = STARTED
            slider.setAutoDraw(True)
        
        # if slider is active this frame...
        if slider.status == STARTED:
            # update params
            pass
        
        # if slider is stopping this frame...
        if slider.status == STARTED:
            if bool(slider_placeholder == 1):
                # keep track of stop time/frame for later
                slider.tStop = t  # not accounting for scr refresh
                slider.tStopRefresh = tThisFlipGlobal  # on global time
                slider.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider.stopped')
                # update status
                slider.status = FINISHED
                slider.setAutoDraw(False)
        
        # *ansTag* updates
        
        # if ansTag is starting this frame...
        if ansTag.status == NOT_STARTED and slider_placeholder == 1:
            # keep track of start time/frame for later
            ansTag.frameNStart = frameN  # exact frame index
            ansTag.tStart = t  # local t and not account for scr refresh
            ansTag.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ansTag, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ansTag.started')
            # update status
            ansTag.status = STARTED
            ansTag.setAutoDraw(True)
        
        # if ansTag is active this frame...
        if ansTag.status == STARTED:
            # update params
            ansTag.setPos((-0.72, AnsY), log=False)
        
        # *noAnsTag* updates
        
        # if noAnsTag is starting this frame...
        if noAnsTag.status == NOT_STARTED and slider_placeholder == 1:
            # keep track of start time/frame for later
            noAnsTag.frameNStart = frameN  # exact frame index
            noAnsTag.tStart = t  # local t and not account for scr refresh
            noAnsTag.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(noAnsTag, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'noAnsTag.started')
            # update status
            noAnsTag.status = STARTED
            noAnsTag.setAutoDraw(True)
        
        # if noAnsTag is active this frame...
        if noAnsTag.status == STARTED:
            # update params
            noAnsTag.setPos((-0.72, NoAnsY), log=False)
        # Run 'Each Frame' code from code_2
        if slider_placeholder != 1:
            if slider.getRating() == 1:
                AnsY = upper_ansYH
                NoAnsY = lower_ansTH
                slider_placeholder = 1
                selection_time = datetime.datetime.now()
            elif slider.getRating() == 2:
                AnsY = lower_ansTH
                NoAnsY = upper_ansYH
                slider_placeholder = 1
                selection_time = datetime.datetime.now()
        if slider_placeholder == 1 and next_button_enable == 0:
            elapsed = (datetime.datetime.now() - selection_time).total_seconds()
            if elapsed >= 3:
                next_button_enable = 1
        
        # *ino_answer* updates
        
        # if ino_answer is starting this frame...
        if ino_answer.status == NOT_STARTED and inoculation_switch == 1 and slider_placeholder == 1:
            # keep track of start time/frame for later
            ino_answer.frameNStart = frameN  # exact frame index
            ino_answer.tStart = t  # local t and not account for scr refresh
            ino_answer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ino_answer, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ino_answer.started')
            # update status
            ino_answer.status = STARTED
            ino_answer.setAutoDraw(True)
        
        # if ino_answer is active this frame...
        if ino_answer.status == STARTED:
            # update params
            pass
        
        # *nonino_answer* updates
        
        # if nonino_answer is starting this frame...
        if nonino_answer.status == NOT_STARTED and inoculation_switch == 0 and slider_placeholder == 1:
            # keep track of start time/frame for later
            nonino_answer.frameNStart = frameN  # exact frame index
            nonino_answer.tStart = t  # local t and not account for scr refresh
            nonino_answer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nonino_answer, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'nonino_answer.started')
            # update status
            nonino_answer.status = STARTED
            nonino_answer.setAutoDraw(True)
        
        # if nonino_answer is active this frame...
        if nonino_answer.status == STARTED:
            # update params
            pass
        
        # *btn_rev_img* updates
        
        # if btn_rev_img is starting this frame...
        if btn_rev_img.status == NOT_STARTED and next_button_enable == 1:
            # keep track of start time/frame for later
            btn_rev_img.frameNStart = frameN  # exact frame index
            btn_rev_img.tStart = t  # local t and not account for scr refresh
            btn_rev_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(btn_rev_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'btn_rev_img.started')
            # update status
            btn_rev_img.status = STARTED
            btn_rev_img.setAutoDraw(True)
        
        # if btn_rev_img is active this frame...
        if btn_rev_img.status == STARTED:
            # update params
            pass
        # Run 'Each Frame' code from btn_rev_img_2
        # 滑鼠位置
        mouseX, mouseY = mouse_rev.getPos()
        
        # 圖片邊界
        btn_left = btn_rev_img.pos[0] - btn_rev_img.size[0]/2
        btn_right = btn_rev_img.pos[0] + btn_rev_img.size[0]/2
        btn_top = btn_rev_img.pos[1] + btn_rev_img.size[1]/2
        btn_bottom = btn_rev_img.pos[1] - btn_rev_img.size[1]/2
        
        # 檢查滑鼠是否在圖片上
        if btn_left <= mouseX <= btn_right and btn_bottom <= mouseY <= btn_top:
            btn_rev_img.image = 'highlight_next_btn.png'  # 滑鼠移到上面時，換成高亮圖片
        else:
            btn_rev_img.image = 'normal_next_btn.png'     # 滑鼠移開時，換回原圖
        
        # *mouse_rev* updates
        
        # if mouse_rev is starting this frame...
        if mouse_rev.status == NOT_STARTED and next_button_enable == 1:
            # keep track of start time/frame for later
            mouse_rev.frameNStart = frameN  # exact frame index
            mouse_rev.tStart = t  # local t and not account for scr refresh
            mouse_rev.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_rev, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_rev.started', t)
            # update status
            mouse_rev.status = STARTED
            mouse_rev.mouseClock.reset()
            prevButtonState = mouse_rev.getPressed()  # if button is down already this ISN'T a new click
        if mouse_rev.status == STARTED:  # only update if started and not finished!
            buttons = mouse_rev.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(btn_rev_img, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_rev):
                            gotValidClick = True
                            mouse_rev.clicked_name.append(obj.name)
                    if not gotValidClick:
                        mouse_rev.clicked_name.append(None)
                    x, y = mouse_rev.getPos()
                    mouse_rev.x.append(x)
                    mouse_rev.y.append(y)
                    buttons = mouse_rev.getPressed()
                    mouse_rev.leftButton.append(buttons[0])
                    mouse_rev.midButton.append(buttons[1])
                    mouse_rev.rightButton.append(buttons[2])
                    mouse_rev.time.append(mouse_rev.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
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
                currentRoutine=Review_trial,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Review_trial.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Review_trial.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Review_trial" ---
    for thisComponent in Review_trial.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Review_trial
    Review_trial.tStop = globalClock.getTime(format='float')
    Review_trial.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Review_trial.stopped', Review_trial.tStop)
    thisExp.addData('slider.response', slider.getRating())
    thisExp.addData('slider.rt', slider.getRT())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_rev.x', mouse_rev.x)
    thisExp.addData('mouse_rev.y', mouse_rev.y)
    thisExp.addData('mouse_rev.leftButton', mouse_rev.leftButton)
    thisExp.addData('mouse_rev.midButton', mouse_rev.midButton)
    thisExp.addData('mouse_rev.rightButton', mouse_rev.rightButton)
    thisExp.addData('mouse_rev.time', mouse_rev.time)
    thisExp.addData('mouse_rev.clicked_name', mouse_rev.clicked_name)
    thisExp.nextEntry()
    # the Routine "Review_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Start_Of_Practice" ---
    # create an object to store info about Routine Start_Of_Practice
    Start_Of_Practice = data.Routine(
        name='Start_Of_Practice',
        components=[text_norm_2, btn6_img, mouse6],
    )
    Start_Of_Practice.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse6
    mouse6.x = []
    mouse6.y = []
    mouse6.leftButton = []
    mouse6.midButton = []
    mouse6.rightButton = []
    mouse6.time = []
    mouse6.clicked_name = []
    gotValidClick = False  # until a click is received
    # store start times for Start_Of_Practice
    Start_Of_Practice.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Start_Of_Practice.tStart = globalClock.getTime(format='float')
    Start_Of_Practice.status = STARTED
    thisExp.addData('Start_Of_Practice.started', Start_Of_Practice.tStart)
    Start_Of_Practice.maxDuration = None
    # keep track of which components have finished
    Start_Of_PracticeComponents = Start_Of_Practice.components
    for thisComponent in Start_Of_Practice.components:
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
    
    # --- Run Routine "Start_Of_Practice" ---
    Start_Of_Practice.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_norm_2* updates
        
        # if text_norm_2 is starting this frame...
        if text_norm_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_norm_2.frameNStart = frameN  # exact frame index
            text_norm_2.tStart = t  # local t and not account for scr refresh
            text_norm_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_norm_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_norm_2.status = STARTED
            text_norm_2.setAutoDraw(True)
        
        # if text_norm_2 is active this frame...
        if text_norm_2.status == STARTED:
            # update params
            pass
        
        # *btn6_img* updates
        
        # if btn6_img is starting this frame...
        if btn6_img.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            btn6_img.frameNStart = frameN  # exact frame index
            btn6_img.tStart = t  # local t and not account for scr refresh
            btn6_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(btn6_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'btn6_img.started')
            # update status
            btn6_img.status = STARTED
            btn6_img.setAutoDraw(True)
        
        # if btn6_img is active this frame...
        if btn6_img.status == STARTED:
            # update params
            pass
        # Run 'Each Frame' code from btn6_color_code
        # 滑鼠位置
        mouseX, mouseY = mouse6.getPos()
        
        # 圖片邊界
        btn_left = btn6_img.pos[0] - btn6_img.size[0]/2
        btn_right = btn6_img.pos[0] + btn6_img.size[0]/2
        btn_top = btn6_img.pos[1] + btn6_img.size[1]/2
        btn_bottom = btn6_img.pos[1] - btn6_img.size[1]/2
        
        # 檢查滑鼠是否在圖片上
        if btn_left <= mouseX <= btn_right and btn_bottom <= mouseY <= btn_top:
            btn6_img.image = 'highlight_next_btn.png'  # 滑鼠移到上面時，換成高亮圖片
        else:
            btn6_img.image = 'normal_next_btn.png'     # 滑鼠移開時，換回原圖
        
        # *mouse6* updates
        
        # if mouse6 is starting this frame...
        if mouse6.status == NOT_STARTED and t >= mouse_debounce_timeout-frameTolerance:
            # keep track of start time/frame for later
            mouse6.frameNStart = frameN  # exact frame index
            mouse6.tStart = t  # local t and not account for scr refresh
            mouse6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse6.started', t)
            # update status
            mouse6.status = STARTED
            mouse6.mouseClock.reset()
            prevButtonState = mouse6.getPressed()  # if button is down already this ISN'T a new click
        if mouse6.status == STARTED:  # only update if started and not finished!
            buttons = mouse6.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(btn6_img, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse6):
                            gotValidClick = True
                            mouse6.clicked_name.append(obj.name)
                    if not gotValidClick:
                        mouse6.clicked_name.append(None)
                    x, y = mouse6.getPos()
                    mouse6.x.append(x)
                    mouse6.y.append(y)
                    buttons = mouse6.getPressed()
                    mouse6.leftButton.append(buttons[0])
                    mouse6.midButton.append(buttons[1])
                    mouse6.rightButton.append(buttons[2])
                    mouse6.time.append(mouse6.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
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
                currentRoutine=Start_Of_Practice,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Start_Of_Practice.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Start_Of_Practice.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Start_Of_Practice" ---
    for thisComponent in Start_Of_Practice.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Start_Of_Practice
    Start_Of_Practice.tStop = globalClock.getTime(format='float')
    Start_Of_Practice.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Start_Of_Practice.stopped', Start_Of_Practice.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse6.x', mouse6.x)
    thisExp.addData('mouse6.y', mouse6.y)
    thisExp.addData('mouse6.leftButton', mouse6.leftButton)
    thisExp.addData('mouse6.midButton', mouse6.midButton)
    thisExp.addData('mouse6.rightButton', mouse6.rightButton)
    thisExp.addData('mouse6.time', mouse6.time)
    thisExp.addData('mouse6.clicked_name', mouse6.clicked_name)
    thisExp.nextEntry()
    # the Routine "Start_Of_Practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practice_loop = data.TrialHandler2(
        name='practice_loop',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions(
        'prac_stim_cb_lookup.csv', 
        selection='[0,1,2]'
    )
    , 
        seed=None, 
    )
    thisExp.addLoop(practice_loop)  # add the loop to the experiment
    thisPractice_loop = practice_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
    if thisPractice_loop != None:
        for paramName in thisPractice_loop:
            globals()[paramName] = thisPractice_loop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisPractice_loop in practice_loop:
        practice_loop.status = STARTED
        if hasattr(thisPractice_loop, 'status'):
            thisPractice_loop.status = STARTED
        currentLoop = practice_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
        if thisPractice_loop != None:
            for paramName in thisPractice_loop:
                globals()[paramName] = thisPractice_loop[paramName]
        
        # --- Prepare to start Routine "prepare_stim" ---
        # create an object to store info about Routine prepare_stim
        prepare_stim = data.Routine(
            name='prepare_stim',
            components=[],
        )
        prepare_stim.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from prepare_stim_code
        #stim_heightX = scale_stim_ratio*(stim_pic_sizeY/stim_pic_sizeX)
        #stim_heightY = scale_stim_ratio
        stim_heightX = scale_stim_maxY * (stim_pic_sizeX / stim_pic_sizeY)
        stim_heightY = scale_stim_maxY
        if stim_heightX > scale_stim_maxX:
            stim_heightY = stim_heightY / (stim_heightX / scale_stim_maxX)
            stim_heightX = scale_stim_maxX
        # store start times for prepare_stim
        prepare_stim.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        prepare_stim.tStart = globalClock.getTime(format='float')
        prepare_stim.status = STARTED
        thisExp.addData('prepare_stim.started', prepare_stim.tStart)
        prepare_stim.maxDuration = None
        # keep track of which components have finished
        prepare_stimComponents = prepare_stim.components
        for thisComponent in prepare_stim.components:
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
        
        # --- Run Routine "prepare_stim" ---
        prepare_stim.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisPractice_loop, 'status') and thisPractice_loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
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
                    currentRoutine=prepare_stim,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                prepare_stim.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prepare_stim.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "prepare_stim" ---
        for thisComponent in prepare_stim.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for prepare_stim
        prepare_stim.tStop = globalClock.getTime(format='float')
        prepare_stim.tStopRefresh = tThisFlipGlobal
        thisExp.addData('prepare_stim.stopped', prepare_stim.tStop)
        # the Routine "prepare_stim" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "stimuli_img" ---
        # create an object to store info about Routine stimuli_img
        stimuli_img = data.Routine(
            name='stimuli_img',
            components=[stim_img, btn7_img, mouse7],
        )
        stimuli_img.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        stim_img.setSize([stim_heightX,stim_heightY])
        stim_img.setImage(stim_picname)
        # setup some python lists for storing info about the mouse7
        mouse7.x = []
        mouse7.y = []
        mouse7.leftButton = []
        mouse7.midButton = []
        mouse7.rightButton = []
        mouse7.time = []
        mouse7.clicked_name = []
        gotValidClick = False  # until a click is received
        # store start times for stimuli_img
        stimuli_img.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        stimuli_img.tStart = globalClock.getTime(format='float')
        stimuli_img.status = STARTED
        thisExp.addData('stimuli_img.started', stimuli_img.tStart)
        stimuli_img.maxDuration = None
        # keep track of which components have finished
        stimuli_imgComponents = stimuli_img.components
        for thisComponent in stimuli_img.components:
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
        
        # --- Run Routine "stimuli_img" ---
        stimuli_img.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisPractice_loop, 'status') and thisPractice_loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stim_img* updates
            
            # if stim_img is starting this frame...
            if stim_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim_img.frameNStart = frameN  # exact frame index
                stim_img.tStart = t  # local t and not account for scr refresh
                stim_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stim_img.started')
                # update status
                stim_img.status = STARTED
                stim_img.setAutoDraw(True)
            
            # if stim_img is active this frame...
            if stim_img.status == STARTED:
                # update params
                pass
            
            # *btn7_img* updates
            
            # if btn7_img is starting this frame...
            if btn7_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                btn7_img.frameNStart = frameN  # exact frame index
                btn7_img.tStart = t  # local t and not account for scr refresh
                btn7_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(btn7_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'btn7_img.started')
                # update status
                btn7_img.status = STARTED
                btn7_img.setAutoDraw(True)
            
            # if btn7_img is active this frame...
            if btn7_img.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from btn7_color_code
            # 滑鼠位置
            mouseX, mouseY = mouse7.getPos()
            
            # 圖片邊界
            btn_left = btn7_img.pos[0] - btn7_img.size[0]/2
            btn_right = btn7_img.pos[0] + btn7_img.size[0]/2
            btn_top = btn7_img.pos[1] + btn7_img.size[1]/2
            btn_bottom = btn7_img.pos[1] - btn7_img.size[1]/2
            
            # 檢查滑鼠是否在圖片上
            if btn_left <= mouseX <= btn_right and btn_bottom <= mouseY <= btn_top:
                btn7_img.image = 'highlight_next_btn.png'  # 滑鼠移到上面時，換成高亮圖片
            else:
                btn7_img.image = 'normal_next_btn.png'     # 滑鼠移開時，換回原圖
            
            # *mouse7* updates
            
            # if mouse7 is starting this frame...
            if mouse7.status == NOT_STARTED and t >= mouse_debounce_timeout-frameTolerance:
                # keep track of start time/frame for later
                mouse7.frameNStart = frameN  # exact frame index
                mouse7.tStart = t  # local t and not account for scr refresh
                mouse7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse7.started', t)
                # update status
                mouse7.status = STARTED
                mouse7.mouseClock.reset()
                prevButtonState = mouse7.getPressed()  # if button is down already this ISN'T a new click
            if mouse7.status == STARTED:  # only update if started and not finished!
                buttons = mouse7.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames(btn7_img, namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse7):
                                gotValidClick = True
                                mouse7.clicked_name.append(obj.name)
                        if not gotValidClick:
                            mouse7.clicked_name.append(None)
                        x, y = mouse7.getPos()
                        mouse7.x.append(x)
                        mouse7.y.append(y)
                        buttons = mouse7.getPressed()
                        mouse7.leftButton.append(buttons[0])
                        mouse7.midButton.append(buttons[1])
                        mouse7.rightButton.append(buttons[2])
                        mouse7.time.append(mouse7.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
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
                    currentRoutine=stimuli_img,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                stimuli_img.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stimuli_img.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "stimuli_img" ---
        for thisComponent in stimuli_img.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for stimuli_img
        stimuli_img.tStop = globalClock.getTime(format='float')
        stimuli_img.tStopRefresh = tThisFlipGlobal
        thisExp.addData('stimuli_img.stopped', stimuli_img.tStop)
        # store data for practice_loop (TrialHandler)
        practice_loop.addData('mouse7.x', mouse7.x)
        practice_loop.addData('mouse7.y', mouse7.y)
        practice_loop.addData('mouse7.leftButton', mouse7.leftButton)
        practice_loop.addData('mouse7.midButton', mouse7.midButton)
        practice_loop.addData('mouse7.rightButton', mouse7.rightButton)
        practice_loop.addData('mouse7.time', mouse7.time)
        practice_loop.addData('mouse7.clicked_name', mouse7.clicked_name)
        # the Routine "stimuli_img" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        resp_prac_loop = data.TrialHandler2(
            name='resp_prac_loop',
            nReps=1.0, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions(
            'prac_resp_type_lookup.csv', 
            selection=practice_loop_special_setting
        )
        , 
            seed=None, 
        )
        thisExp.addLoop(resp_prac_loop)  # add the loop to the experiment
        thisResp_prac_loop = resp_prac_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisResp_prac_loop.rgb)
        if thisResp_prac_loop != None:
            for paramName in thisResp_prac_loop:
                globals()[paramName] = thisResp_prac_loop[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisResp_prac_loop in resp_prac_loop:
            resp_prac_loop.status = STARTED
            if hasattr(thisResp_prac_loop, 'status'):
                thisResp_prac_loop.status = STARTED
            currentLoop = resp_prac_loop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisResp_prac_loop.rgb)
            if thisResp_prac_loop != None:
                for paramName in thisResp_prac_loop:
                    globals()[paramName] = thisResp_prac_loop[paramName]
            
            # --- Prepare to start Routine "resp_mixed" ---
            # create an object to store info about Routine resp_mixed
            resp_mixed = data.Routine(
                name='resp_mixed',
                components=[we_banner, tof_banner, att_banner, true_or_false, tof_indicator, pre_indicator, which_emoji, attitude_bg, attitude, btn8_img, mouse8, we_bg, stim_thumbnail],
            )
            resp_mixed.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            true_or_false.reset()
            pre_indicator.setText(pre_ind_text)
            which_emoji.reset()
            attitude.reset()
            # Run 'Begin Routine' code from code_4
            true_or_false.rating = 5
            attitude.rating = 5.5
            pre_tof_status = 1
            attitude.line.size=(dv_wlong,30 * (screenX/screenY/form_related_ratio))
            # setup some python lists for storing info about the mouse8
            mouse8.x = []
            mouse8.y = []
            mouse8.leftButton = []
            mouse8.midButton = []
            mouse8.rightButton = []
            mouse8.time = []
            mouse8.clicked_name = []
            gotValidClick = False  # until a click is received
            stim_thumbnail.setPos((0, aaaaaaaaaaaaaaaaaaaaaaaa * screenY))
            stim_thumbnail.setSize([stim_heightX*thumbnail_to_screen_scale_factor,stim_heightY*thumbnail_to_screen_scale_factor])
            stim_thumbnail.setImage(stim_picname)
            # store start times for resp_mixed
            resp_mixed.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            resp_mixed.tStart = globalClock.getTime(format='float')
            resp_mixed.status = STARTED
            thisExp.addData('resp_mixed.started', resp_mixed.tStart)
            resp_mixed.maxDuration = None
            # keep track of which components have finished
            resp_mixedComponents = resp_mixed.components
            for thisComponent in resp_mixed.components:
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
            
            # --- Run Routine "resp_mixed" ---
            resp_mixed.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisResp_prac_loop, 'status') and thisResp_prac_loop.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *we_banner* updates
                
                # if we_banner is starting this frame...
                if we_banner.status == NOT_STARTED and resp_switch == 2:
                    # keep track of start time/frame for later
                    we_banner.frameNStart = frameN  # exact frame index
                    we_banner.tStart = t  # local t and not account for scr refresh
                    we_banner.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(we_banner, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'we_banner.started')
                    # update status
                    we_banner.status = STARTED
                    we_banner.setAutoDraw(True)
                
                # if we_banner is active this frame...
                if we_banner.status == STARTED:
                    # update params
                    pass
                
                # *tof_banner* updates
                
                # if tof_banner is starting this frame...
                if tof_banner.status == NOT_STARTED and resp_switch == 1:
                    # keep track of start time/frame for later
                    tof_banner.frameNStart = frameN  # exact frame index
                    tof_banner.tStart = t  # local t and not account for scr refresh
                    tof_banner.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(tof_banner, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'tof_banner.started')
                    # update status
                    tof_banner.status = STARTED
                    tof_banner.setAutoDraw(True)
                
                # if tof_banner is active this frame...
                if tof_banner.status == STARTED:
                    # update params
                    pass
                
                # *att_banner* updates
                
                # if att_banner is starting this frame...
                if att_banner.status == NOT_STARTED and resp_switch == 3:
                    # keep track of start time/frame for later
                    att_banner.frameNStart = frameN  # exact frame index
                    att_banner.tStart = t  # local t and not account for scr refresh
                    att_banner.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(att_banner, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'att_banner.started')
                    # update status
                    att_banner.status = STARTED
                    att_banner.setAutoDraw(True)
                
                # if att_banner is active this frame...
                if att_banner.status == STARTED:
                    # update params
                    pass
                
                # *true_or_false* updates
                
                # if true_or_false is starting this frame...
                if true_or_false.status == NOT_STARTED and resp_switch == 1:
                    # keep track of start time/frame for later
                    true_or_false.frameNStart = frameN  # exact frame index
                    true_or_false.tStart = t  # local t and not account for scr refresh
                    true_or_false.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(true_or_false, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'true_or_false.started')
                    # update status
                    true_or_false.status = STARTED
                    true_or_false.setAutoDraw(True)
                
                # if true_or_false is active this frame...
                if true_or_false.status == STARTED:
                    # update params
                    pass
                
                # *tof_indicator* updates
                
                # if tof_indicator is starting this frame...
                if tof_indicator.status == NOT_STARTED and resp_switch == 1 and pre_tof_status == 0:
                    # keep track of start time/frame for later
                    tof_indicator.frameNStart = frameN  # exact frame index
                    tof_indicator.tStart = t  # local t and not account for scr refresh
                    tof_indicator.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(tof_indicator, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'tof_indicator.started')
                    # update status
                    tof_indicator.status = STARTED
                    tof_indicator.setAutoDraw(True)
                
                # if tof_indicator is active this frame...
                if tof_indicator.status == STARTED:
                    # update params
                    tof_indicator.setText(round(true_or_false.getRating(),2), log=False)
                
                # *pre_indicator* updates
                
                # if pre_indicator is starting this frame...
                if pre_indicator.status == NOT_STARTED and pre_tof_status == 1:
                    # keep track of start time/frame for later
                    pre_indicator.frameNStart = frameN  # exact frame index
                    pre_indicator.tStart = t  # local t and not account for scr refresh
                    pre_indicator.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pre_indicator, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'pre_indicator.started')
                    # update status
                    pre_indicator.status = STARTED
                    pre_indicator.setAutoDraw(True)
                
                # if pre_indicator is active this frame...
                if pre_indicator.status == STARTED:
                    # update params
                    pass
                
                # if pre_indicator is stopping this frame...
                if pre_indicator.status == STARTED:
                    if bool(pre_tof_status == 0):
                        # keep track of stop time/frame for later
                        pre_indicator.tStop = t  # not accounting for scr refresh
                        pre_indicator.tStopRefresh = tThisFlipGlobal  # on global time
                        pre_indicator.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'pre_indicator.stopped')
                        # update status
                        pre_indicator.status = FINISHED
                        pre_indicator.setAutoDraw(False)
                
                # *which_emoji* updates
                
                # if which_emoji is starting this frame...
                if which_emoji.status == NOT_STARTED and resp_switch == 2:
                    # keep track of start time/frame for later
                    which_emoji.frameNStart = frameN  # exact frame index
                    which_emoji.tStart = t  # local t and not account for scr refresh
                    which_emoji.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(which_emoji, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'which_emoji.started')
                    # update status
                    which_emoji.status = STARTED
                    which_emoji.setAutoDraw(True)
                
                # if which_emoji is active this frame...
                if which_emoji.status == STARTED:
                    # update params
                    pass
                
                # *attitude_bg* updates
                
                # if attitude_bg is starting this frame...
                if attitude_bg.status == NOT_STARTED and resp_switch == 3:
                    # keep track of start time/frame for later
                    attitude_bg.frameNStart = frameN  # exact frame index
                    attitude_bg.tStart = t  # local t and not account for scr refresh
                    attitude_bg.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(attitude_bg, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'attitude_bg.started')
                    # update status
                    attitude_bg.status = STARTED
                    attitude_bg.setAutoDraw(True)
                
                # if attitude_bg is active this frame...
                if attitude_bg.status == STARTED:
                    # update params
                    pass
                
                # *attitude* updates
                
                # if attitude is starting this frame...
                if attitude.status == NOT_STARTED and resp_switch == 3:
                    # keep track of start time/frame for later
                    attitude.frameNStart = frameN  # exact frame index
                    attitude.tStart = t  # local t and not account for scr refresh
                    attitude.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(attitude, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'attitude.started')
                    # update status
                    attitude.status = STARTED
                    attitude.setAutoDraw(True)
                
                # if attitude is active this frame...
                if attitude.status == STARTED:
                    # update params
                    pass
                # Run 'Each Frame' code from code_4
                if true_or_false.rating != 5 or which_emoji.rating or attitude.rating != 5.5:
                    pre_tof_status = 0
                
                
                # *btn8_img* updates
                
                # if btn8_img is starting this frame...
                if btn8_img.status == NOT_STARTED and pre_tof_status == 0:
                    # keep track of start time/frame for later
                    btn8_img.frameNStart = frameN  # exact frame index
                    btn8_img.tStart = t  # local t and not account for scr refresh
                    btn8_img.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(btn8_img, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'btn8_img.started')
                    # update status
                    btn8_img.status = STARTED
                    btn8_img.setAutoDraw(True)
                
                # if btn8_img is active this frame...
                if btn8_img.status == STARTED:
                    # update params
                    pass
                # Run 'Each Frame' code from btn8_color_code
                # 滑鼠位置
                mouseX, mouseY = mouse8.getPos()
                
                # 圖片邊界
                btn_left = btn8_img.pos[0] - btn8_img.size[0]/2
                btn_right = btn8_img.pos[0] + btn8_img.size[0]/2
                btn_top = btn8_img.pos[1] + btn8_img.size[1]/2
                btn_bottom = btn8_img.pos[1] - btn8_img.size[1]/2
                
                # 檢查滑鼠是否在圖片上
                if btn_left <= mouseX <= btn_right and btn_bottom <= mouseY <= btn_top:
                    btn8_img.image = 'highlight_next_btn.png'  # 滑鼠移到上面時，換成高亮圖片
                else:
                    btn8_img.image = 'normal_next_btn.png'     # 滑鼠移開時，換回原圖
                
                # *mouse8* updates
                
                # if mouse8 is starting this frame...
                if mouse8.status == NOT_STARTED and pre_tof_status == 0:
                    # keep track of start time/frame for later
                    mouse8.frameNStart = frameN  # exact frame index
                    mouse8.tStart = t  # local t and not account for scr refresh
                    mouse8.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse8, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('mouse8.started', t)
                    # update status
                    mouse8.status = STARTED
                    mouse8.mouseClock.reset()
                    prevButtonState = mouse8.getPressed()  # if button is down already this ISN'T a new click
                if mouse8.status == STARTED:  # only update if started and not finished!
                    buttons = mouse8.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            clickableList = environmenttools.getFromNames(btn8_img, namespace=locals())
                            for obj in clickableList:
                                # is this object clicked on?
                                if obj.contains(mouse8):
                                    gotValidClick = True
                                    mouse8.clicked_name.append(obj.name)
                            if not gotValidClick:
                                mouse8.clicked_name.append(None)
                            x, y = mouse8.getPos()
                            mouse8.x.append(x)
                            mouse8.y.append(y)
                            buttons = mouse8.getPressed()
                            mouse8.leftButton.append(buttons[0])
                            mouse8.midButton.append(buttons[1])
                            mouse8.rightButton.append(buttons[2])
                            mouse8.time.append(mouse8.mouseClock.getTime())
                            if gotValidClick:
                                continueRoutine = False  # end routine on response
                
                # *we_bg* updates
                
                # if we_bg is starting this frame...
                if we_bg.status == NOT_STARTED and resp_switch == 2:
                    # keep track of start time/frame for later
                    we_bg.frameNStart = frameN  # exact frame index
                    we_bg.tStart = t  # local t and not account for scr refresh
                    we_bg.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(we_bg, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'we_bg.started')
                    # update status
                    we_bg.status = STARTED
                    we_bg.setAutoDraw(True)
                
                # if we_bg is active this frame...
                if we_bg.status == STARTED:
                    # update params
                    pass
                
                # *stim_thumbnail* updates
                
                # if stim_thumbnail is starting this frame...
                if stim_thumbnail.status == NOT_STARTED and resp_switch != 2:
                    # keep track of start time/frame for later
                    stim_thumbnail.frameNStart = frameN  # exact frame index
                    stim_thumbnail.tStart = t  # local t and not account for scr refresh
                    stim_thumbnail.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stim_thumbnail, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stim_thumbnail.started')
                    # update status
                    stim_thumbnail.status = STARTED
                    stim_thumbnail.setAutoDraw(True)
                
                # if stim_thumbnail is active this frame...
                if stim_thumbnail.status == STARTED:
                    # update params
                    pass
                
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
                        currentRoutine=resp_mixed,
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    resp_mixed.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in resp_mixed.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "resp_mixed" ---
            for thisComponent in resp_mixed.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for resp_mixed
            resp_mixed.tStop = globalClock.getTime(format='float')
            resp_mixed.tStopRefresh = tThisFlipGlobal
            thisExp.addData('resp_mixed.stopped', resp_mixed.tStop)
            resp_prac_loop.addData('true_or_false.response', true_or_false.getRating())
            resp_prac_loop.addData('true_or_false.rt', true_or_false.getRT())
            resp_prac_loop.addData('which_emoji.response', which_emoji.getRating())
            resp_prac_loop.addData('which_emoji.rt', which_emoji.getRT())
            resp_prac_loop.addData('attitude.response', attitude.getRating())
            resp_prac_loop.addData('attitude.rt', attitude.getRT())
            # store data for resp_prac_loop (TrialHandler)
            resp_prac_loop.addData('mouse8.x', mouse8.x)
            resp_prac_loop.addData('mouse8.y', mouse8.y)
            resp_prac_loop.addData('mouse8.leftButton', mouse8.leftButton)
            resp_prac_loop.addData('mouse8.midButton', mouse8.midButton)
            resp_prac_loop.addData('mouse8.rightButton', mouse8.rightButton)
            resp_prac_loop.addData('mouse8.time', mouse8.time)
            resp_prac_loop.addData('mouse8.clicked_name', mouse8.clicked_name)
            # the Routine "resp_mixed" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            # mark thisResp_prac_loop as finished
            if hasattr(thisResp_prac_loop, 'status'):
                thisResp_prac_loop.status = FINISHED
            # if awaiting a pause, pause now
            if resp_prac_loop.status == PAUSED:
                thisExp.status = PAUSED
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[globalClock], 
                )
                # once done pausing, restore running status
                resp_prac_loop.status = STARTED
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'resp_prac_loop'
        resp_prac_loop.status = FINISHED
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # mark thisPractice_loop as finished
        if hasattr(thisPractice_loop, 'status'):
            thisPractice_loop.status = FINISHED
        # if awaiting a pause, pause now
        if practice_loop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            practice_loop.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'practice_loop'
    practice_loop.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "End_Of_Practice" ---
    # create an object to store info about Routine End_Of_Practice
    End_Of_Practice = data.Routine(
        name='End_Of_Practice',
        components=[text_norm_3, btn9_img, mouse9],
    )
    End_Of_Practice.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse9
    mouse9.x = []
    mouse9.y = []
    mouse9.leftButton = []
    mouse9.midButton = []
    mouse9.rightButton = []
    mouse9.time = []
    mouse9.clicked_name = []
    gotValidClick = False  # until a click is received
    # store start times for End_Of_Practice
    End_Of_Practice.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    End_Of_Practice.tStart = globalClock.getTime(format='float')
    End_Of_Practice.status = STARTED
    thisExp.addData('End_Of_Practice.started', End_Of_Practice.tStart)
    End_Of_Practice.maxDuration = None
    # keep track of which components have finished
    End_Of_PracticeComponents = End_Of_Practice.components
    for thisComponent in End_Of_Practice.components:
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
    
    # --- Run Routine "End_Of_Practice" ---
    End_Of_Practice.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_norm_3* updates
        
        # if text_norm_3 is starting this frame...
        if text_norm_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_norm_3.frameNStart = frameN  # exact frame index
            text_norm_3.tStart = t  # local t and not account for scr refresh
            text_norm_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_norm_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_norm_3.status = STARTED
            text_norm_3.setAutoDraw(True)
        
        # if text_norm_3 is active this frame...
        if text_norm_3.status == STARTED:
            # update params
            pass
        
        # *btn9_img* updates
        
        # if btn9_img is starting this frame...
        if btn9_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            btn9_img.frameNStart = frameN  # exact frame index
            btn9_img.tStart = t  # local t and not account for scr refresh
            btn9_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(btn9_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'btn9_img.started')
            # update status
            btn9_img.status = STARTED
            btn9_img.setAutoDraw(True)
        
        # if btn9_img is active this frame...
        if btn9_img.status == STARTED:
            # update params
            pass
        # Run 'Each Frame' code from btn9_color_code
        # 滑鼠位置
        mouseX, mouseY = mouse9.getPos()
        
        # 圖片邊界
        btn_left = btn9_img.pos[0] - btn9_img.size[0]/2
        btn_right = btn9_img.pos[0] + btn9_img.size[0]/2
        btn_top = btn9_img.pos[1] + btn9_img.size[1]/2
        btn_bottom = btn9_img.pos[1] - btn9_img.size[1]/2
        
        # 檢查滑鼠是否在圖片上
        if btn_left <= mouseX <= btn_right and btn_bottom <= mouseY <= btn_top:
            btn9_img.image = 'highlight_next_btn.png'  # 滑鼠移到上面時，換成高亮圖片
        else:
            btn9_img.image = 'normal_next_btn.png'     # 滑鼠移開時，換回原圖
        
        # *mouse9* updates
        
        # if mouse9 is starting this frame...
        if mouse9.status == NOT_STARTED and t >= mouse_debounce_timeout-frameTolerance:
            # keep track of start time/frame for later
            mouse9.frameNStart = frameN  # exact frame index
            mouse9.tStart = t  # local t and not account for scr refresh
            mouse9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse9.started', t)
            # update status
            mouse9.status = STARTED
            mouse9.mouseClock.reset()
            prevButtonState = mouse9.getPressed()  # if button is down already this ISN'T a new click
        if mouse9.status == STARTED:  # only update if started and not finished!
            buttons = mouse9.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(btn9_img, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse9):
                            gotValidClick = True
                            mouse9.clicked_name.append(obj.name)
                    if not gotValidClick:
                        mouse9.clicked_name.append(None)
                    x, y = mouse9.getPos()
                    mouse9.x.append(x)
                    mouse9.y.append(y)
                    buttons = mouse9.getPressed()
                    mouse9.leftButton.append(buttons[0])
                    mouse9.midButton.append(buttons[1])
                    mouse9.rightButton.append(buttons[2])
                    mouse9.time.append(mouse9.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
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
                currentRoutine=End_Of_Practice,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            End_Of_Practice.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End_Of_Practice.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "End_Of_Practice" ---
    for thisComponent in End_Of_Practice.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for End_Of_Practice
    End_Of_Practice.tStop = globalClock.getTime(format='float')
    End_Of_Practice.tStopRefresh = tThisFlipGlobal
    thisExp.addData('End_Of_Practice.stopped', End_Of_Practice.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse9.x', mouse9.x)
    thisExp.addData('mouse9.y', mouse9.y)
    thisExp.addData('mouse9.leftButton', mouse9.leftButton)
    thisExp.addData('mouse9.midButton', mouse9.midButton)
    thisExp.addData('mouse9.rightButton', mouse9.rightButton)
    thisExp.addData('mouse9.time', mouse9.time)
    thisExp.addData('mouse9.clicked_name', mouse9.clicked_name)
    thisExp.nextEntry()
    # the Routine "End_Of_Practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    main_loop = data.TrialHandler2(
        name='main_loop',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions(
        'main_stim_cb_lookup.csv', 
        selection=trial_order
    )
    , 
        seed=None, 
    )
    thisExp.addLoop(main_loop)  # add the loop to the experiment
    thisMain_loop = main_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMain_loop.rgb)
    if thisMain_loop != None:
        for paramName in thisMain_loop:
            globals()[paramName] = thisMain_loop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisMain_loop in main_loop:
        main_loop.status = STARTED
        if hasattr(thisMain_loop, 'status'):
            thisMain_loop.status = STARTED
        currentLoop = main_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisMain_loop.rgb)
        if thisMain_loop != None:
            for paramName in thisMain_loop:
                globals()[paramName] = thisMain_loop[paramName]
        
        # --- Prepare to start Routine "prepare_stim" ---
        # create an object to store info about Routine prepare_stim
        prepare_stim = data.Routine(
            name='prepare_stim',
            components=[],
        )
        prepare_stim.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from prepare_stim_code
        #stim_heightX = scale_stim_ratio*(stim_pic_sizeY/stim_pic_sizeX)
        #stim_heightY = scale_stim_ratio
        stim_heightX = scale_stim_maxY * (stim_pic_sizeX / stim_pic_sizeY)
        stim_heightY = scale_stim_maxY
        if stim_heightX > scale_stim_maxX:
            stim_heightY = stim_heightY / (stim_heightX / scale_stim_maxX)
            stim_heightX = scale_stim_maxX
        # store start times for prepare_stim
        prepare_stim.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        prepare_stim.tStart = globalClock.getTime(format='float')
        prepare_stim.status = STARTED
        thisExp.addData('prepare_stim.started', prepare_stim.tStart)
        prepare_stim.maxDuration = None
        # keep track of which components have finished
        prepare_stimComponents = prepare_stim.components
        for thisComponent in prepare_stim.components:
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
        
        # --- Run Routine "prepare_stim" ---
        prepare_stim.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisMain_loop, 'status') and thisMain_loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
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
                    currentRoutine=prepare_stim,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                prepare_stim.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prepare_stim.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "prepare_stim" ---
        for thisComponent in prepare_stim.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for prepare_stim
        prepare_stim.tStop = globalClock.getTime(format='float')
        prepare_stim.tStopRefresh = tThisFlipGlobal
        thisExp.addData('prepare_stim.stopped', prepare_stim.tStop)
        # the Routine "prepare_stim" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "stimuli_img" ---
        # create an object to store info about Routine stimuli_img
        stimuli_img = data.Routine(
            name='stimuli_img',
            components=[stim_img, btn7_img, mouse7],
        )
        stimuli_img.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        stim_img.setSize([stim_heightX,stim_heightY])
        stim_img.setImage(stim_picname)
        # setup some python lists for storing info about the mouse7
        mouse7.x = []
        mouse7.y = []
        mouse7.leftButton = []
        mouse7.midButton = []
        mouse7.rightButton = []
        mouse7.time = []
        mouse7.clicked_name = []
        gotValidClick = False  # until a click is received
        # store start times for stimuli_img
        stimuli_img.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        stimuli_img.tStart = globalClock.getTime(format='float')
        stimuli_img.status = STARTED
        thisExp.addData('stimuli_img.started', stimuli_img.tStart)
        stimuli_img.maxDuration = None
        # keep track of which components have finished
        stimuli_imgComponents = stimuli_img.components
        for thisComponent in stimuli_img.components:
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
        
        # --- Run Routine "stimuli_img" ---
        stimuli_img.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisMain_loop, 'status') and thisMain_loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stim_img* updates
            
            # if stim_img is starting this frame...
            if stim_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim_img.frameNStart = frameN  # exact frame index
                stim_img.tStart = t  # local t and not account for scr refresh
                stim_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stim_img.started')
                # update status
                stim_img.status = STARTED
                stim_img.setAutoDraw(True)
            
            # if stim_img is active this frame...
            if stim_img.status == STARTED:
                # update params
                pass
            
            # *btn7_img* updates
            
            # if btn7_img is starting this frame...
            if btn7_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                btn7_img.frameNStart = frameN  # exact frame index
                btn7_img.tStart = t  # local t and not account for scr refresh
                btn7_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(btn7_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'btn7_img.started')
                # update status
                btn7_img.status = STARTED
                btn7_img.setAutoDraw(True)
            
            # if btn7_img is active this frame...
            if btn7_img.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from btn7_color_code
            # 滑鼠位置
            mouseX, mouseY = mouse7.getPos()
            
            # 圖片邊界
            btn_left = btn7_img.pos[0] - btn7_img.size[0]/2
            btn_right = btn7_img.pos[0] + btn7_img.size[0]/2
            btn_top = btn7_img.pos[1] + btn7_img.size[1]/2
            btn_bottom = btn7_img.pos[1] - btn7_img.size[1]/2
            
            # 檢查滑鼠是否在圖片上
            if btn_left <= mouseX <= btn_right and btn_bottom <= mouseY <= btn_top:
                btn7_img.image = 'highlight_next_btn.png'  # 滑鼠移到上面時，換成高亮圖片
            else:
                btn7_img.image = 'normal_next_btn.png'     # 滑鼠移開時，換回原圖
            
            # *mouse7* updates
            
            # if mouse7 is starting this frame...
            if mouse7.status == NOT_STARTED and t >= mouse_debounce_timeout-frameTolerance:
                # keep track of start time/frame for later
                mouse7.frameNStart = frameN  # exact frame index
                mouse7.tStart = t  # local t and not account for scr refresh
                mouse7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse7.started', t)
                # update status
                mouse7.status = STARTED
                mouse7.mouseClock.reset()
                prevButtonState = mouse7.getPressed()  # if button is down already this ISN'T a new click
            if mouse7.status == STARTED:  # only update if started and not finished!
                buttons = mouse7.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames(btn7_img, namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse7):
                                gotValidClick = True
                                mouse7.clicked_name.append(obj.name)
                        if not gotValidClick:
                            mouse7.clicked_name.append(None)
                        x, y = mouse7.getPos()
                        mouse7.x.append(x)
                        mouse7.y.append(y)
                        buttons = mouse7.getPressed()
                        mouse7.leftButton.append(buttons[0])
                        mouse7.midButton.append(buttons[1])
                        mouse7.rightButton.append(buttons[2])
                        mouse7.time.append(mouse7.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
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
                    currentRoutine=stimuli_img,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                stimuli_img.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stimuli_img.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "stimuli_img" ---
        for thisComponent in stimuli_img.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for stimuli_img
        stimuli_img.tStop = globalClock.getTime(format='float')
        stimuli_img.tStopRefresh = tThisFlipGlobal
        thisExp.addData('stimuli_img.stopped', stimuli_img.tStop)
        # store data for main_loop (TrialHandler)
        main_loop.addData('mouse7.x', mouse7.x)
        main_loop.addData('mouse7.y', mouse7.y)
        main_loop.addData('mouse7.leftButton', mouse7.leftButton)
        main_loop.addData('mouse7.midButton', mouse7.midButton)
        main_loop.addData('mouse7.rightButton', mouse7.rightButton)
        main_loop.addData('mouse7.time', mouse7.time)
        main_loop.addData('mouse7.clicked_name', mouse7.clicked_name)
        # the Routine "stimuli_img" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "prepare_resp_order" ---
        # create an object to store info about Routine prepare_resp_order
        prepare_resp_order = data.Routine(
            name='prepare_resp_order',
            components=[],
        )
        prepare_resp_order.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_5
        #extract the current resp_order unit
        #to let the script know what order we'll use in this trial round
        resp_order_unit_raw = resp_order_list.pop(0)
        resp_order_unit = [i-1 for i in resp_order_unit_raw]
        # store start times for prepare_resp_order
        prepare_resp_order.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        prepare_resp_order.tStart = globalClock.getTime(format='float')
        prepare_resp_order.status = STARTED
        thisExp.addData('prepare_resp_order.started', prepare_resp_order.tStart)
        prepare_resp_order.maxDuration = None
        # keep track of which components have finished
        prepare_resp_orderComponents = prepare_resp_order.components
        for thisComponent in prepare_resp_order.components:
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
        
        # --- Run Routine "prepare_resp_order" ---
        prepare_resp_order.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisMain_loop, 'status') and thisMain_loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
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
                    currentRoutine=prepare_resp_order,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                prepare_resp_order.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prepare_resp_order.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "prepare_resp_order" ---
        for thisComponent in prepare_resp_order.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for prepare_resp_order
        prepare_resp_order.tStop = globalClock.getTime(format='float')
        prepare_resp_order.tStopRefresh = tThisFlipGlobal
        thisExp.addData('prepare_resp_order.stopped', prepare_resp_order.tStop)
        # the Routine "prepare_resp_order" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        resp_main_loop = data.TrialHandler2(
            name='resp_main_loop',
            nReps=1.0, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions(
            'prac_resp_type_lookup.csv', 
            selection=resp_order_unit
        )
        , 
            seed=None, 
        )
        thisExp.addLoop(resp_main_loop)  # add the loop to the experiment
        thisResp_main_loop = resp_main_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisResp_main_loop.rgb)
        if thisResp_main_loop != None:
            for paramName in thisResp_main_loop:
                globals()[paramName] = thisResp_main_loop[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisResp_main_loop in resp_main_loop:
            resp_main_loop.status = STARTED
            if hasattr(thisResp_main_loop, 'status'):
                thisResp_main_loop.status = STARTED
            currentLoop = resp_main_loop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisResp_main_loop.rgb)
            if thisResp_main_loop != None:
                for paramName in thisResp_main_loop:
                    globals()[paramName] = thisResp_main_loop[paramName]
            
            # --- Prepare to start Routine "resp_mixed" ---
            # create an object to store info about Routine resp_mixed
            resp_mixed = data.Routine(
                name='resp_mixed',
                components=[we_banner, tof_banner, att_banner, true_or_false, tof_indicator, pre_indicator, which_emoji, attitude_bg, attitude, btn8_img, mouse8, we_bg, stim_thumbnail],
            )
            resp_mixed.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            true_or_false.reset()
            pre_indicator.setText(pre_ind_text)
            which_emoji.reset()
            attitude.reset()
            # Run 'Begin Routine' code from code_4
            true_or_false.rating = 5
            attitude.rating = 5.5
            pre_tof_status = 1
            attitude.line.size=(dv_wlong,30 * (screenX/screenY/form_related_ratio))
            # setup some python lists for storing info about the mouse8
            mouse8.x = []
            mouse8.y = []
            mouse8.leftButton = []
            mouse8.midButton = []
            mouse8.rightButton = []
            mouse8.time = []
            mouse8.clicked_name = []
            gotValidClick = False  # until a click is received
            stim_thumbnail.setPos((0, aaaaaaaaaaaaaaaaaaaaaaaa * screenY))
            stim_thumbnail.setSize([stim_heightX*thumbnail_to_screen_scale_factor,stim_heightY*thumbnail_to_screen_scale_factor])
            stim_thumbnail.setImage(stim_picname)
            # store start times for resp_mixed
            resp_mixed.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            resp_mixed.tStart = globalClock.getTime(format='float')
            resp_mixed.status = STARTED
            thisExp.addData('resp_mixed.started', resp_mixed.tStart)
            resp_mixed.maxDuration = None
            # keep track of which components have finished
            resp_mixedComponents = resp_mixed.components
            for thisComponent in resp_mixed.components:
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
            
            # --- Run Routine "resp_mixed" ---
            resp_mixed.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisResp_main_loop, 'status') and thisResp_main_loop.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *we_banner* updates
                
                # if we_banner is starting this frame...
                if we_banner.status == NOT_STARTED and resp_switch == 2:
                    # keep track of start time/frame for later
                    we_banner.frameNStart = frameN  # exact frame index
                    we_banner.tStart = t  # local t and not account for scr refresh
                    we_banner.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(we_banner, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'we_banner.started')
                    # update status
                    we_banner.status = STARTED
                    we_banner.setAutoDraw(True)
                
                # if we_banner is active this frame...
                if we_banner.status == STARTED:
                    # update params
                    pass
                
                # *tof_banner* updates
                
                # if tof_banner is starting this frame...
                if tof_banner.status == NOT_STARTED and resp_switch == 1:
                    # keep track of start time/frame for later
                    tof_banner.frameNStart = frameN  # exact frame index
                    tof_banner.tStart = t  # local t and not account for scr refresh
                    tof_banner.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(tof_banner, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'tof_banner.started')
                    # update status
                    tof_banner.status = STARTED
                    tof_banner.setAutoDraw(True)
                
                # if tof_banner is active this frame...
                if tof_banner.status == STARTED:
                    # update params
                    pass
                
                # *att_banner* updates
                
                # if att_banner is starting this frame...
                if att_banner.status == NOT_STARTED and resp_switch == 3:
                    # keep track of start time/frame for later
                    att_banner.frameNStart = frameN  # exact frame index
                    att_banner.tStart = t  # local t and not account for scr refresh
                    att_banner.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(att_banner, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'att_banner.started')
                    # update status
                    att_banner.status = STARTED
                    att_banner.setAutoDraw(True)
                
                # if att_banner is active this frame...
                if att_banner.status == STARTED:
                    # update params
                    pass
                
                # *true_or_false* updates
                
                # if true_or_false is starting this frame...
                if true_or_false.status == NOT_STARTED and resp_switch == 1:
                    # keep track of start time/frame for later
                    true_or_false.frameNStart = frameN  # exact frame index
                    true_or_false.tStart = t  # local t and not account for scr refresh
                    true_or_false.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(true_or_false, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'true_or_false.started')
                    # update status
                    true_or_false.status = STARTED
                    true_or_false.setAutoDraw(True)
                
                # if true_or_false is active this frame...
                if true_or_false.status == STARTED:
                    # update params
                    pass
                
                # *tof_indicator* updates
                
                # if tof_indicator is starting this frame...
                if tof_indicator.status == NOT_STARTED and resp_switch == 1 and pre_tof_status == 0:
                    # keep track of start time/frame for later
                    tof_indicator.frameNStart = frameN  # exact frame index
                    tof_indicator.tStart = t  # local t and not account for scr refresh
                    tof_indicator.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(tof_indicator, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'tof_indicator.started')
                    # update status
                    tof_indicator.status = STARTED
                    tof_indicator.setAutoDraw(True)
                
                # if tof_indicator is active this frame...
                if tof_indicator.status == STARTED:
                    # update params
                    tof_indicator.setText(round(true_or_false.getRating(),2), log=False)
                
                # *pre_indicator* updates
                
                # if pre_indicator is starting this frame...
                if pre_indicator.status == NOT_STARTED and pre_tof_status == 1:
                    # keep track of start time/frame for later
                    pre_indicator.frameNStart = frameN  # exact frame index
                    pre_indicator.tStart = t  # local t and not account for scr refresh
                    pre_indicator.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pre_indicator, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'pre_indicator.started')
                    # update status
                    pre_indicator.status = STARTED
                    pre_indicator.setAutoDraw(True)
                
                # if pre_indicator is active this frame...
                if pre_indicator.status == STARTED:
                    # update params
                    pass
                
                # if pre_indicator is stopping this frame...
                if pre_indicator.status == STARTED:
                    if bool(pre_tof_status == 0):
                        # keep track of stop time/frame for later
                        pre_indicator.tStop = t  # not accounting for scr refresh
                        pre_indicator.tStopRefresh = tThisFlipGlobal  # on global time
                        pre_indicator.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'pre_indicator.stopped')
                        # update status
                        pre_indicator.status = FINISHED
                        pre_indicator.setAutoDraw(False)
                
                # *which_emoji* updates
                
                # if which_emoji is starting this frame...
                if which_emoji.status == NOT_STARTED and resp_switch == 2:
                    # keep track of start time/frame for later
                    which_emoji.frameNStart = frameN  # exact frame index
                    which_emoji.tStart = t  # local t and not account for scr refresh
                    which_emoji.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(which_emoji, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'which_emoji.started')
                    # update status
                    which_emoji.status = STARTED
                    which_emoji.setAutoDraw(True)
                
                # if which_emoji is active this frame...
                if which_emoji.status == STARTED:
                    # update params
                    pass
                
                # *attitude_bg* updates
                
                # if attitude_bg is starting this frame...
                if attitude_bg.status == NOT_STARTED and resp_switch == 3:
                    # keep track of start time/frame for later
                    attitude_bg.frameNStart = frameN  # exact frame index
                    attitude_bg.tStart = t  # local t and not account for scr refresh
                    attitude_bg.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(attitude_bg, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'attitude_bg.started')
                    # update status
                    attitude_bg.status = STARTED
                    attitude_bg.setAutoDraw(True)
                
                # if attitude_bg is active this frame...
                if attitude_bg.status == STARTED:
                    # update params
                    pass
                
                # *attitude* updates
                
                # if attitude is starting this frame...
                if attitude.status == NOT_STARTED and resp_switch == 3:
                    # keep track of start time/frame for later
                    attitude.frameNStart = frameN  # exact frame index
                    attitude.tStart = t  # local t and not account for scr refresh
                    attitude.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(attitude, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'attitude.started')
                    # update status
                    attitude.status = STARTED
                    attitude.setAutoDraw(True)
                
                # if attitude is active this frame...
                if attitude.status == STARTED:
                    # update params
                    pass
                # Run 'Each Frame' code from code_4
                if true_or_false.rating != 5 or which_emoji.rating or attitude.rating != 5.5:
                    pre_tof_status = 0
                
                
                # *btn8_img* updates
                
                # if btn8_img is starting this frame...
                if btn8_img.status == NOT_STARTED and pre_tof_status == 0:
                    # keep track of start time/frame for later
                    btn8_img.frameNStart = frameN  # exact frame index
                    btn8_img.tStart = t  # local t and not account for scr refresh
                    btn8_img.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(btn8_img, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'btn8_img.started')
                    # update status
                    btn8_img.status = STARTED
                    btn8_img.setAutoDraw(True)
                
                # if btn8_img is active this frame...
                if btn8_img.status == STARTED:
                    # update params
                    pass
                # Run 'Each Frame' code from btn8_color_code
                # 滑鼠位置
                mouseX, mouseY = mouse8.getPos()
                
                # 圖片邊界
                btn_left = btn8_img.pos[0] - btn8_img.size[0]/2
                btn_right = btn8_img.pos[0] + btn8_img.size[0]/2
                btn_top = btn8_img.pos[1] + btn8_img.size[1]/2
                btn_bottom = btn8_img.pos[1] - btn8_img.size[1]/2
                
                # 檢查滑鼠是否在圖片上
                if btn_left <= mouseX <= btn_right and btn_bottom <= mouseY <= btn_top:
                    btn8_img.image = 'highlight_next_btn.png'  # 滑鼠移到上面時，換成高亮圖片
                else:
                    btn8_img.image = 'normal_next_btn.png'     # 滑鼠移開時，換回原圖
                
                # *mouse8* updates
                
                # if mouse8 is starting this frame...
                if mouse8.status == NOT_STARTED and pre_tof_status == 0:
                    # keep track of start time/frame for later
                    mouse8.frameNStart = frameN  # exact frame index
                    mouse8.tStart = t  # local t and not account for scr refresh
                    mouse8.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse8, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('mouse8.started', t)
                    # update status
                    mouse8.status = STARTED
                    mouse8.mouseClock.reset()
                    prevButtonState = mouse8.getPressed()  # if button is down already this ISN'T a new click
                if mouse8.status == STARTED:  # only update if started and not finished!
                    buttons = mouse8.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            clickableList = environmenttools.getFromNames(btn8_img, namespace=locals())
                            for obj in clickableList:
                                # is this object clicked on?
                                if obj.contains(mouse8):
                                    gotValidClick = True
                                    mouse8.clicked_name.append(obj.name)
                            if not gotValidClick:
                                mouse8.clicked_name.append(None)
                            x, y = mouse8.getPos()
                            mouse8.x.append(x)
                            mouse8.y.append(y)
                            buttons = mouse8.getPressed()
                            mouse8.leftButton.append(buttons[0])
                            mouse8.midButton.append(buttons[1])
                            mouse8.rightButton.append(buttons[2])
                            mouse8.time.append(mouse8.mouseClock.getTime())
                            if gotValidClick:
                                continueRoutine = False  # end routine on response
                
                # *we_bg* updates
                
                # if we_bg is starting this frame...
                if we_bg.status == NOT_STARTED and resp_switch == 2:
                    # keep track of start time/frame for later
                    we_bg.frameNStart = frameN  # exact frame index
                    we_bg.tStart = t  # local t and not account for scr refresh
                    we_bg.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(we_bg, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'we_bg.started')
                    # update status
                    we_bg.status = STARTED
                    we_bg.setAutoDraw(True)
                
                # if we_bg is active this frame...
                if we_bg.status == STARTED:
                    # update params
                    pass
                
                # *stim_thumbnail* updates
                
                # if stim_thumbnail is starting this frame...
                if stim_thumbnail.status == NOT_STARTED and resp_switch != 2:
                    # keep track of start time/frame for later
                    stim_thumbnail.frameNStart = frameN  # exact frame index
                    stim_thumbnail.tStart = t  # local t and not account for scr refresh
                    stim_thumbnail.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stim_thumbnail, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stim_thumbnail.started')
                    # update status
                    stim_thumbnail.status = STARTED
                    stim_thumbnail.setAutoDraw(True)
                
                # if stim_thumbnail is active this frame...
                if stim_thumbnail.status == STARTED:
                    # update params
                    pass
                
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
                        currentRoutine=resp_mixed,
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    resp_mixed.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in resp_mixed.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "resp_mixed" ---
            for thisComponent in resp_mixed.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for resp_mixed
            resp_mixed.tStop = globalClock.getTime(format='float')
            resp_mixed.tStopRefresh = tThisFlipGlobal
            thisExp.addData('resp_mixed.stopped', resp_mixed.tStop)
            resp_main_loop.addData('true_or_false.response', true_or_false.getRating())
            resp_main_loop.addData('true_or_false.rt', true_or_false.getRT())
            resp_main_loop.addData('which_emoji.response', which_emoji.getRating())
            resp_main_loop.addData('which_emoji.rt', which_emoji.getRT())
            resp_main_loop.addData('attitude.response', attitude.getRating())
            resp_main_loop.addData('attitude.rt', attitude.getRT())
            # store data for resp_main_loop (TrialHandler)
            resp_main_loop.addData('mouse8.x', mouse8.x)
            resp_main_loop.addData('mouse8.y', mouse8.y)
            resp_main_loop.addData('mouse8.leftButton', mouse8.leftButton)
            resp_main_loop.addData('mouse8.midButton', mouse8.midButton)
            resp_main_loop.addData('mouse8.rightButton', mouse8.rightButton)
            resp_main_loop.addData('mouse8.time', mouse8.time)
            resp_main_loop.addData('mouse8.clicked_name', mouse8.clicked_name)
            # the Routine "resp_mixed" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            # mark thisResp_main_loop as finished
            if hasattr(thisResp_main_loop, 'status'):
                thisResp_main_loop.status = FINISHED
            # if awaiting a pause, pause now
            if resp_main_loop.status == PAUSED:
                thisExp.status = PAUSED
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[globalClock], 
                )
                # once done pausing, restore running status
                resp_main_loop.status = STARTED
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'resp_main_loop'
        resp_main_loop.status = FINISHED
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # mark thisMain_loop as finished
        if hasattr(thisMain_loop, 'status'):
            thisMain_loop.status = FINISHED
        # if awaiting a pause, pause now
        if main_loop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            main_loop.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'main_loop'
    main_loop.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "End_Of_Main_Trial" ---
    # create an object to store info about Routine End_Of_Main_Trial
    End_Of_Main_Trial = data.Routine(
        name='End_Of_Main_Trial',
        components=[text_norm_4, btn10_img, mouse10],
    )
    End_Of_Main_Trial.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse10
    mouse10.x = []
    mouse10.y = []
    mouse10.leftButton = []
    mouse10.midButton = []
    mouse10.rightButton = []
    mouse10.time = []
    mouse10.clicked_name = []
    gotValidClick = False  # until a click is received
    # store start times for End_Of_Main_Trial
    End_Of_Main_Trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    End_Of_Main_Trial.tStart = globalClock.getTime(format='float')
    End_Of_Main_Trial.status = STARTED
    thisExp.addData('End_Of_Main_Trial.started', End_Of_Main_Trial.tStart)
    End_Of_Main_Trial.maxDuration = None
    # keep track of which components have finished
    End_Of_Main_TrialComponents = End_Of_Main_Trial.components
    for thisComponent in End_Of_Main_Trial.components:
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
    
    # --- Run Routine "End_Of_Main_Trial" ---
    End_Of_Main_Trial.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_norm_4* updates
        
        # if text_norm_4 is starting this frame...
        if text_norm_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_norm_4.frameNStart = frameN  # exact frame index
            text_norm_4.tStart = t  # local t and not account for scr refresh
            text_norm_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_norm_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_norm_4.status = STARTED
            text_norm_4.setAutoDraw(True)
        
        # if text_norm_4 is active this frame...
        if text_norm_4.status == STARTED:
            # update params
            pass
        
        # *btn10_img* updates
        
        # if btn10_img is starting this frame...
        if btn10_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            btn10_img.frameNStart = frameN  # exact frame index
            btn10_img.tStart = t  # local t and not account for scr refresh
            btn10_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(btn10_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'btn10_img.started')
            # update status
            btn10_img.status = STARTED
            btn10_img.setAutoDraw(True)
        
        # if btn10_img is active this frame...
        if btn10_img.status == STARTED:
            # update params
            pass
        # Run 'Each Frame' code from btn10_color_code
        # 滑鼠位置
        mouseX, mouseY = mouse10.getPos()
        
        # 圖片邊界
        btn_left = btn10_img.pos[0] - btn10_img.size[0]/2
        btn_right = btn10_img.pos[0] + btn10_img.size[0]/2
        btn_top = btn10_img.pos[1] + btn10_img.size[1]/2
        btn_bottom = btn10_img.pos[1] - btn10_img.size[1]/2
        
        # 檢查滑鼠是否在圖片上
        if btn_left <= mouseX <= btn_right and btn_bottom <= mouseY <= btn_top:
            btn10_img.image = 'highlight_next_btn.png'  # 滑鼠移到上面時，換成高亮圖片
        else:
            btn10_img.image = 'normal_next_btn.png'     # 滑鼠移開時，換回原圖
        
        # *mouse10* updates
        
        # if mouse10 is starting this frame...
        if mouse10.status == NOT_STARTED and t >= mouse_debounce_timeout-frameTolerance:
            # keep track of start time/frame for later
            mouse10.frameNStart = frameN  # exact frame index
            mouse10.tStart = t  # local t and not account for scr refresh
            mouse10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse10.started', t)
            # update status
            mouse10.status = STARTED
            mouse10.mouseClock.reset()
            prevButtonState = mouse10.getPressed()  # if button is down already this ISN'T a new click
        if mouse10.status == STARTED:  # only update if started and not finished!
            buttons = mouse10.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(btn10_img, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse10):
                            gotValidClick = True
                            mouse10.clicked_name.append(obj.name)
                    if not gotValidClick:
                        mouse10.clicked_name.append(None)
                    x, y = mouse10.getPos()
                    mouse10.x.append(x)
                    mouse10.y.append(y)
                    buttons = mouse10.getPressed()
                    mouse10.leftButton.append(buttons[0])
                    mouse10.midButton.append(buttons[1])
                    mouse10.rightButton.append(buttons[2])
                    mouse10.time.append(mouse10.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
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
                currentRoutine=End_Of_Main_Trial,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            End_Of_Main_Trial.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End_Of_Main_Trial.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "End_Of_Main_Trial" ---
    for thisComponent in End_Of_Main_Trial.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for End_Of_Main_Trial
    End_Of_Main_Trial.tStop = globalClock.getTime(format='float')
    End_Of_Main_Trial.tStopRefresh = tThisFlipGlobal
    thisExp.addData('End_Of_Main_Trial.stopped', End_Of_Main_Trial.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse10.x', mouse10.x)
    thisExp.addData('mouse10.y', mouse10.y)
    thisExp.addData('mouse10.leftButton', mouse10.leftButton)
    thisExp.addData('mouse10.midButton', mouse10.midButton)
    thisExp.addData('mouse10.rightButton', mouse10.rightButton)
    thisExp.addData('mouse10.time', mouse10.time)
    thisExp.addData('mouse10.clicked_name', mouse10.clicked_name)
    thisExp.nextEntry()
    # the Routine "End_Of_Main_Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Political_Prefs_Form" ---
    # create an object to store info about Routine Political_Prefs_Form
    Political_Prefs_Form = data.Routine(
        name='Political_Prefs_Form',
        components=[PBF_form, btn3_img, mouse3, pre_indicator_2],
    )
    Political_Prefs_Form.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse3
    mouse3.x = []
    mouse3.y = []
    mouse3.leftButton = []
    mouse3.midButton = []
    mouse3.rightButton = []
    mouse3.time = []
    mouse3.clicked_name = []
    gotValidClick = False  # until a click is received
    # store start times for Political_Prefs_Form
    Political_Prefs_Form.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Political_Prefs_Form.tStart = globalClock.getTime(format='float')
    Political_Prefs_Form.status = STARTED
    thisExp.addData('Political_Prefs_Form.started', Political_Prefs_Form.tStart)
    Political_Prefs_Form.maxDuration = None
    # keep track of which components have finished
    Political_Prefs_FormComponents = Political_Prefs_Form.components
    for thisComponent in Political_Prefs_Form.components:
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
    
    # --- Run Routine "Political_Prefs_Form" ---
    Political_Prefs_Form.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *PBF_form* updates
        
        # if PBF_form is starting this frame...
        if PBF_form.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PBF_form.frameNStart = frameN  # exact frame index
            PBF_form.tStart = t  # local t and not account for scr refresh
            PBF_form.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PBF_form, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PBF_form.started')
            # update status
            PBF_form.status = STARTED
            PBF_form.setAutoDraw(True)
        
        # if PBF_form is active this frame...
        if PBF_form.status == STARTED:
            # update params
            pass
        
        # *btn3_img* updates
        
        # if btn3_img is starting this frame...
        if btn3_img.status == NOT_STARTED and PBF_form.complete:
            # keep track of start time/frame for later
            btn3_img.frameNStart = frameN  # exact frame index
            btn3_img.tStart = t  # local t and not account for scr refresh
            btn3_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(btn3_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'btn3_img.started')
            # update status
            btn3_img.status = STARTED
            btn3_img.setAutoDraw(True)
        
        # if btn3_img is active this frame...
        if btn3_img.status == STARTED:
            # update params
            pass
        # Run 'Each Frame' code from btn3_color_code
        # 滑鼠位置
        mouseX, mouseY = mouse3.getPos()
        
        # 圖片邊界
        btn_left = btn3_img.pos[0] - btn3_img.size[0]/2
        btn_right = btn3_img.pos[0] + btn3_img.size[0]/2
        btn_top = btn3_img.pos[1] + btn3_img.size[1]/2
        btn_bottom = btn3_img.pos[1] - btn3_img.size[1]/2
        
        # 檢查滑鼠是否在圖片上
        if btn_left <= mouseX <= btn_right and btn_bottom <= mouseY <= btn_top:
            btn3_img.image = 'highlight_next_btn.png'  # 滑鼠移到上面時，換成高亮圖片
        else:
            btn3_img.image = 'normal_next_btn.png'     # 滑鼠移開時，換回原圖
        
        # *mouse3* updates
        
        # if mouse3 is starting this frame...
        if mouse3.status == NOT_STARTED and PBF_form.complete:
            # keep track of start time/frame for later
            mouse3.frameNStart = frameN  # exact frame index
            mouse3.tStart = t  # local t and not account for scr refresh
            mouse3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse3.started', t)
            # update status
            mouse3.status = STARTED
            mouse3.mouseClock.reset()
            prevButtonState = mouse3.getPressed()  # if button is down already this ISN'T a new click
        if mouse3.status == STARTED:  # only update if started and not finished!
            buttons = mouse3.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(btn3_img, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse3):
                            gotValidClick = True
                            mouse3.clicked_name.append(obj.name)
                    if not gotValidClick:
                        mouse3.clicked_name.append(None)
                    x, y = mouse3.getPos()
                    mouse3.x.append(x)
                    mouse3.y.append(y)
                    buttons = mouse3.getPressed()
                    mouse3.leftButton.append(buttons[0])
                    mouse3.midButton.append(buttons[1])
                    mouse3.rightButton.append(buttons[2])
                    mouse3.time.append(mouse3.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # *pre_indicator_2* updates
        
        # if pre_indicator_2 is starting this frame...
        if pre_indicator_2.status == NOT_STARTED and not PBF_form.complete:
            # keep track of start time/frame for later
            pre_indicator_2.frameNStart = frameN  # exact frame index
            pre_indicator_2.tStart = t  # local t and not account for scr refresh
            pre_indicator_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pre_indicator_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pre_indicator_2.started')
            # update status
            pre_indicator_2.status = STARTED
            pre_indicator_2.setAutoDraw(True)
        
        # if pre_indicator_2 is active this frame...
        if pre_indicator_2.status == STARTED:
            # update params
            pass
        
        # if pre_indicator_2 is stopping this frame...
        if pre_indicator_2.status == STARTED:
            if bool(PBF_form.complete):
                # keep track of stop time/frame for later
                pre_indicator_2.tStop = t  # not accounting for scr refresh
                pre_indicator_2.tStopRefresh = tThisFlipGlobal  # on global time
                pre_indicator_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pre_indicator_2.stopped')
                # update status
                pre_indicator_2.status = FINISHED
                pre_indicator_2.setAutoDraw(False)
        
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
                currentRoutine=Political_Prefs_Form,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Political_Prefs_Form.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Political_Prefs_Form.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Political_Prefs_Form" ---
    for thisComponent in Political_Prefs_Form.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Political_Prefs_Form
    Political_Prefs_Form.tStop = globalClock.getTime(format='float')
    Political_Prefs_Form.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Political_Prefs_Form.stopped', Political_Prefs_Form.tStop)
    PBF_form.addDataToExp(thisExp, 'rows')
    PBF_form.autodraw = False
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse3.x', mouse3.x)
    thisExp.addData('mouse3.y', mouse3.y)
    thisExp.addData('mouse3.leftButton', mouse3.leftButton)
    thisExp.addData('mouse3.midButton', mouse3.midButton)
    thisExp.addData('mouse3.rightButton', mouse3.rightButton)
    thisExp.addData('mouse3.time', mouse3.time)
    thisExp.addData('mouse3.clicked_name', mouse3.clicked_name)
    thisExp.nextEntry()
    # the Routine "Political_Prefs_Form" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "End_Of_Experiment" ---
    # create an object to store info about Routine End_Of_Experiment
    End_Of_Experiment = data.Routine(
        name='End_Of_Experiment',
        components=[goodbye_text],
    )
    End_Of_Experiment.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for End_Of_Experiment
    End_Of_Experiment.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    End_Of_Experiment.tStart = globalClock.getTime(format='float')
    End_Of_Experiment.status = STARTED
    thisExp.addData('End_Of_Experiment.started', End_Of_Experiment.tStart)
    End_Of_Experiment.maxDuration = None
    # keep track of which components have finished
    End_Of_ExperimentComponents = End_Of_Experiment.components
    for thisComponent in End_Of_Experiment.components:
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
    
    # --- Run Routine "End_Of_Experiment" ---
    End_Of_Experiment.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *goodbye_text* updates
        
        # if goodbye_text is starting this frame...
        if goodbye_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            goodbye_text.frameNStart = frameN  # exact frame index
            goodbye_text.tStart = t  # local t and not account for scr refresh
            goodbye_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(goodbye_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            goodbye_text.status = STARTED
            goodbye_text.setAutoDraw(True)
        
        # if goodbye_text is active this frame...
        if goodbye_text.status == STARTED:
            # update params
            pass
        
        # if goodbye_text is stopping this frame...
        if goodbye_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > goodbye_text.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                goodbye_text.tStop = t  # not accounting for scr refresh
                goodbye_text.tStopRefresh = tThisFlipGlobal  # on global time
                goodbye_text.frameNStop = frameN  # exact frame index
                # update status
                goodbye_text.status = FINISHED
                goodbye_text.setAutoDraw(False)
        
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
                currentRoutine=End_Of_Experiment,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            End_Of_Experiment.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End_Of_Experiment.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "End_Of_Experiment" ---
    for thisComponent in End_Of_Experiment.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for End_Of_Experiment
    End_Of_Experiment.tStop = globalClock.getTime(format='float')
    End_Of_Experiment.tStopRefresh = tThisFlipGlobal
    thisExp.addData('End_Of_Experiment.stopped', End_Of_Experiment.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if End_Of_Experiment.maxDurationReached:
        routineTimer.addTime(-End_Of_Experiment.maxDuration)
    elif End_Of_Experiment.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
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
