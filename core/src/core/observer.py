# -*- python -*-
#
#       OpenAlea.Core: OpenAlea Core 
#
#       Copyright 2006 INRIA - CIRAD - INRA  
#
#       File author(s): Christophe Pradal <christophe.prada@cirad.fr>
#                       Samuel Dufour-Kowalski <samuel.dufour@sophia.inria.fr>
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
# 
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#

__doc__="""
This module defines all the classes for the Observer design Pattern
"""

__license__= "Cecill-C"
__revision__=" $Id$ "

###############################################################################


import weakref


class Observed(object):
    """ Observed Object """

    def __init__(self):

        self.listeners = set()


    def register_listener(self, listener):
        """ Add listener to list of listeners """

        wr = weakref.ref(listener, self.unregister_listener)
        self.listeners.add(wr)
    

    def unregister_listener(self, listener):
        """ Remove listener from the list of listeners """
        self.listeners.discard(listener)


    def notify_listeners(self, event=None):
        """
        Send a notification to all listeners
        @param event : an object to pass to the notify function
        """

        for ref in self.listeners:
            if(not ref().is_notification_locked()):
                try:
                    ref().notify(self, event)
                except Exception, e:
                    print "Warning : notification of %s failed"%(str(ref()),)
                    print e
 

    def __getstate__(self):
        """ Pickle function """
        odict = self.__dict__.copy() 
        odict['listeners'] = set()
        return odict




class AbstractListener(object):
    """ Listener base class """

    notify_lock = None
    
    def initialise (self, observed):
        """ Register self as a listener to observed """
        assert observed != None
        observed.register_listener(self)
        if( self.notify_lock == None) : self.notify_lock = list()


    def is_notification_locked(self):
        return self.notify_lock != None and len(self.notify_lock)>0
        

    def notify (self, sender, event=None):
        """
        This function is called by observed object
        @param sender : the observed object which send notification
        @param event : the data associated to the notification
        """
        raise NotImplementedError()


# Decorator function to protect an AbstractListener against notification
def lock_notify(method):

    def wrapped(self, *args, **kwargs):

        if(self.notify_lock == None) : self.notify_lock = list()
        self.notify_lock.append(True)
        try:
            result = method(self, *args, **kwargs)
        finally:
            self.notify_lock.pop()

        return result
    

    return wrapped


    

