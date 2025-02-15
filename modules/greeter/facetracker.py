# -*- encoding: UTF-8 -*-
import time
import argparse
from naoqi import ALProxy
from tools import *


class FaceTracker(object):

    def __init__(self, session, conf):
        super(FaceTracker, self).__init__()
        self.motion = session.service("ALMotion")
        self.tracker = session.service("ALTracker")
        self.faceWidth = conf["faceWidth"]
        self.maxDistance = conf["maxDistance"]
        self.period = conf["period"]

    def track(self, targetName="Face"):
        self.motion.wakeUp()

        # Add target to track.
        faceWidth = self.faceWidth 
        self.tracker.registerTarget(targetName, faceWidth)
        self.tracker.track(targetName)

        log.info( "ALTracker successfully started.")
        self.tracker.setMaximumDistanceDetection(self.maxDistance)
        self.tracker.setExtractorPeriod(targetName, self.period)

    def stop(self):
        # Stop tracker.
        self.tracker.stopTracker()
        self.tracker.unregisterAllTargets()
        log.info("Tracker stopped.")

