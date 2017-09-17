SP LOG PROXY
============

Summary
-------
This module process MotionCor2 test log, convert it to motioncorr test log, so dosef_logviewer can read it then show graph/curve to cryoEM users.

#Background
##motioncorr
This program corrects whole frame image motion recordded with dose fractionated image stack.
Cite publication: Xueming Li, Paul Mooney, Shawn Zheng, Chris Booth, Michael B. Braunfeld, Sander Gubbens, David A. Agard and Yifan Cheng (2013) Electron counting and beam-induced motion correction enables near atomic resolution single particle cryoEM. Nature Methods, 10, 584-590. PMID: 23644547.
[Visit Website](http://cryoem.ucsf.edu/software/software.html)

##MotionCor2
Correction of electron beam-induced sample motion is one of the major factors contributing to the recent resolution breakthroughs in cryo-electron microscopy. Based on observations that the electron beam induces doming of the thin vitreous ice layer, we developed an algorithm to correct anisotropic image motion at the single pixel level across the whole frame, suitable for both single particle and tomographic images. Iterative, patch-based motion detection is combined with spatial and temporal constraints and dose weighting. The multi-GPU accelerated program, MotionCor2, is sufficiently fast to keep up with automated data collection. The result is an exceptionally robust strategy that can work on a wide range of data sets, including those very close to focus or with very short integration times, obviating the need for particle polishing. Application significantly improves Thon ring quality and 3D reconstruction resolution.
[Visit Website](http://msg.ucsf.edu/em/software/motioncor2.html)

This Git repository convert MotionCor2 log to motioncorr log, so dosef_logviewer (which only can handle motioncorr log) can read converted MotionCor2 log to draw graph.

#Configuration instructions
No need configure

#Installation instructions
No need installation

#Operating instructions
`which MotionCor2` -InMrc Falcon_2012_06_12-14_33_35_0_movie.mrcs -OutMrc Falcon_2012_06_12-14_33_35_0_movie_out.mrcs -LogFile MotionCor2.log0-Full.log
`which python` sp_log_proxy.py --input MotionCor2.log0-Full.log --output motioncorr.sp0.log
`which dosef_logviewer` &

#File manifest
None

#Copyright and licensing information
The sp logproxy program are licensed under the terms of the GNU Public License version 2 (GPLv2).

#Contact information
xiaodong.han@bluejayimaging.com

#Known bugs
None

#Troubleshooting
1. bash: MotionCor2: command not found...
Find the MotionCor2 application first by `find`, then add the path to $PATH environment.
2. python: can't open file 'sp_log_proxy.py': [Errno 2] No such file or directory
Use absolute path of sp_log_proxy.py or run it in the directory of sp_log_proxy.py.
3. bash: dosef_logviewer: command not found...
Find the dosef_logviewer application first by `find`, then add the path to $PATH environment.

#Credits and acknowledgements
Author: xiaodong han

#Changelog
09.17.2017  initial release
