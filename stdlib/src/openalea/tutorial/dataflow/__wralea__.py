
# This file has been generated at Fri Oct 29 12:06:01 2010

from openalea.core import *


__name__ = 'openalea.tutorial.dataflow'

__editable__ = True
__description__ = 'Presents the basics of dataflow usage'
__license__ = 'Cecill-C'
__url__ = ''
__alias__ = ['dataflow']
__version__ = '0.1'
__authors__ = 'Daniel BARBEAU'
__institutes__ = 'INRIA, INRA, CIRAD'
__icon__ = ''


__all__ = ['lazy', '_89955440', '_89955408', 'block']



lazy = CompositeNodeFactory(name='lazy',
                             description='Usage of the lazy flag',
                             category='tutorial',
                             doc='',
                             inputs=[],
                             outputs=[],
                             elt_factory={  2: ('openalea.python method', 'print'),
   3: ('openalea.python method', 'range'),
   4: ('openalea.data structure', 'int'),
   5: ('openalea.data structure', 'int'),
   6: ('openalea.data structure', 'int'),
   7: ('openalea.flow control', 'annotation'),
   8: ('openalea.file.pickle', 'pickle dump'),
   9: ('openalea.file', 'filename'),
   10: ('openalea.file', 'expand_user_dir')},
                             elt_connections={  10023228: (10, 0, 8, 1),
   10023240: (3, 0, 8, 0),
   10023252: (5, 0, 3, 1),
   10023264: (6, 0, 3, 2),
   10023276: (9, 0, 10, 0),
   10023288: (3, 0, 2, 0),
   10023300: (4, 0, 3, 0)},
                             elt_data={  2: {  'block': False,
         'caption': 'print',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x078CFCD0> : "print"',
         'hide': True,
         'id': 2,
         'lazy': False,
         'port_hide_changed': set(),
         'posx': -309.70338857054657,
         'posy': -39.140781246044391,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   3: {  'block': False,
         'caption': 'Simulation',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x078CFC70> : "range"',
         'hide': True,
         'id': 3,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -328.68514381826373,
         'posy': -118.34703665346095,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   4: {  'block': False,
         'caption': '0',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x077BE510> : "int"',
         'hide': True,
         'id': 4,
         'lazy': False,
         'port_hide_changed': set(),
         'posx': -396.82730524835785,
         'posy': -192.69307690360318,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   5: {  'block': False,
         'caption': '10000',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x077BE510> : "int"',
         'hide': True,
         'id': 5,
         'lazy': False,
         'port_hide_changed': set(),
         'posx': -311.19592785382258,
         'posy': -190.52123315281204,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   6: {  'block': False,
         'caption': '2',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x077BE510> : "int"',
         'hide': True,
         'id': 6,
         'lazy': False,
         'port_hide_changed': set(),
         'posx': -202.56455045928726,
         'posy': -190.52123315281202,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   7: {  'factory': '<openalea.core.node.NodeFactory object at 0x07954870> : "annotation"',
         'id': 7,
         'posx': -428.99665847336274,
         'posy': -239.66635816167167,
         'txt': u'The "Simulation" node will run once, and\nafterwards only if any of its inputs changes.'},
   8: {  'block': False,
         'caption': 'pickleToDisk',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x074884F0> : "pickle dump"',
         'hide': True,
         'id': 8,
         'lazy': False,
         'port_hide_changed': set(),
         'posx': -556.4882227548153,
         'posy': -34.327563408678486,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   9: {  'block': False,
         'caption': 'filename',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x078AC0D0> : "filename"',
         'hide': True,
         'id': 9,
         'lazy': False,
         'port_hide_changed': set(),
         'posx': -547.43007941049109,
         'posy': -156.6141148299879,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   10: {  'block': False,
          'caption': 'expand_user_dir',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x07869FD0> : "expand_user_dir"',
          'hide': True,
          'id': 10,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -569.24857603146916,
          'posy': -98.454942395379888,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   '__in__': {  'block': False,
                'caption': 'In',
                'delay': 0,
                'hide': True,
                'id': 0,
                'lazy': True,
                'port_hide_changed': set(),
                'posx': 0,
                'posy': 0,
                'priority': 0,
                'use_user_color': True,
                'user_application': None,
                'user_color': None},
   '__out__': {  'block': False,
                 'caption': 'Out',
                 'delay': 0,
                 'hide': True,
                 'id': 1,
                 'lazy': True,
                 'port_hide_changed': set(),
                 'posx': 0,
                 'posy': 0,
                 'priority': 0,
                 'use_user_color': True,
                 'user_application': None,
                 'user_color': None}},
                             elt_value={  2: [],
   3: [],
   4: [(0, '0')],
   5: [(0, '10000')],
   6: [(0, '2')],
   7: [],
   8: [(2, 'False')],
   9: [(0, "'~/simulationResults.txt'")],
   10: [],
   '__in__': [],
   '__out__': []},
                             elt_ad_hoc={  2: {  'position': [-309.70338857054657, -39.140781246044391],
         'useUserColor': False,
         'userColor': None},
   3: {  'position': [-328.68514381826373, -118.34703665346095],
         'useUserColor': False,
         'userColor': None},
   4: {  'position': [-396.82730524835785, -192.69307690360318],
         'useUserColor': False,
         'userColor': None},
   5: {  'position': [-311.19592785382258, -190.52123315281204],
         'useUserColor': False,
         'userColor': None},
   6: {  'position': [-202.56455045928726, -190.52123315281202],
         'useUserColor': False,
         'userColor': None},
   7: {  'color': None,
         'htmlText': u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n<html><head><meta name="qrichtext" content="1" /><style type="text/css">\np, li { white-space: pre-wrap; }\n</style></head><body style=" font-family:\'Sans\'; font-size:8pt; font-weight:400; font-style:normal;">\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">The &quot;Simulation&quot; node will run once, and</p>\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">afterwards only if any of its inputs changes.</p></body></html>',
         'position': [-428.99665847336274, -239.66635816167167],
         'rectP2': (-1, -1),
         'text': u'The "Simulation" node will run once, and\nafterwards only if any of its inputs changes.',
         'textColor': None,
         'visualStyle': 1},
   8: {  'position': [-556.4882227548153, -34.327563408678486],
         'useUserColor': False,
         'userColor': None},
   9: {  'position': [-547.43007941049109, -156.6141148299879],
         'useUserColor': False,
         'userColor': None},
   10: {  'position': [-569.24857603146916, -98.454942395379888],
          'useUserColor': False,
          'userColor': None},
   '__in__': {  'position': [0, 0], 'useUserColor': True, 'userColor': None},
   '__out__': {  'position': [0, 0], 'useUserColor': True, 'userColor': None}},
                             lazy=True,
                             eval_algo='LambdaEvaluation',
                             )




_89955440 = CompositeNodeFactory(name='evaluation order 2',
                             description='',
                             category='Unclassified',
                             doc='',
                             inputs=[],
                             outputs=[],
                             elt_factory={  2: ('openalea.data structure', 'int'),
   3: ('openalea.numpy.random', 'randn'),
   4: ('openalea.data structure', 'int'),
   5: ('openalea.numpy.math', 'power'),
   6: ('openalea.numpy.math', 'mean'),
   7: ('openalea.flow control', 'annotation'),
   9: ('openalea.pylab.plotting', 'PyLabHist')},
                             elt_connections={  10023216: (2, 0, 9, 2),
   10023240: (5, 0, 9, 1),
   10023264: (3, 0, 6, 0),
   10023276: (3, 0, 5, 0),
   10023288: (4, 0, 5, 1)},
                             elt_data={  2: {  'block': False,
         'caption': '20',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x05341A90> : "int"',
         'hide': True,
         'id': 2,
         'lazy': False,
         'port_hide_changed': set(),
         'posx': 443.75925663230458,
         'posy': -186.13531854601777,
         'priority': 0,
         'use_user_color': False,
         'user_application': False,
         'user_color': None},
   3: {  'block': False,
         'caption': '1 - Input data',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x054E54B0> : "randn"',
         'hide': True,
         'id': 3,
         'lazy': False,
         'port_hide_changed': set(),
         'posx': 249.11810855050493,
         'posy': -264.33211369974435,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   4: {  'block': False,
         'caption': '1',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x05341A90> : "int"',
         'hide': True,
         'id': 4,
         'lazy': False,
         'port_hide_changed': set(),
         'posx': 399.22484671837441,
         'posy': -262.6195983235753,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   5: {  'block': False,
         'caption': '4 - Simulation',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x0533A690> : "power"',
         'hide': True,
         'id': 5,
         'lazy': False,
         'port_hide_changed': set(),
         'posx': 324.29994537344481,
         'posy': -188.141543144369,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   6: {  'block': False,
         'caption': '2 - Mean',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x0533A630> : "mean"',
         'hide': True,
         'id': 6,
         'lazy': False,
         'port_hide_changed': set(),
         'posx': 247.23426028276998,
         'posy': -55.031231525218743,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   7: {  'factory': '<openalea.core.node.NodeFactory object at 0x055D8CB0> : "annotation"',
         'id': 7,
         'posx': 189.08679277147678,
         'posy': -321.8382870719139,
         'txt': u'(a) dataflow evaluation order'},
   9: {  'block': False,
         'caption': 'PostProcessing',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x04FC08B0> : "PyLabHist"',
         'hide': True,
         'id': 9,
         'lazy': False,
         'port_hide_changed': set(),
         'posx': 350.77294679582781,
         'posy': -59.453041829801343,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   '__in__': {  'block': False,
                'caption': 'In',
                'delay': 0,
                'hide': True,
                'id': 0,
                'lazy': True,
                'port_hide_changed': set(),
                'posx': 0,
                'posy': 0,
                'priority': 0,
                'use_user_color': True,
                'user_application': None,
                'user_color': None},
   '__out__': {  'block': False,
                 'caption': 'Out',
                 'delay': 0,
                 'hide': True,
                 'id': 1,
                 'lazy': True,
                 'port_hide_changed': set(),
                 'posx': 0,
                 'posy': 0,
                 'priority': 0,
                 'use_user_color': True,
                 'user_application': None,
                 'user_color': None}},
                             elt_value={  2: [(0, '20')],
   3: [(0, '10000000')],
   4: [(0, '1')],
   5: [],
   6: [(1, 'None'), (2, 'None')],
   7: [],
   9: [  (0, 'None'),
         (3, "'blue'"),
         (4, 'False'),
         (5, 'False'),
         (6, "'bar'"),
         (7, "'mid'"),
         (8, "'vertical'"),
         (9, 'False'),
         (10, "''"),
         (11, '1'),
         (12, "{'alpha': 1.0, 'animated': False}")],
   '__in__': [],
   '__out__': []},
                             elt_ad_hoc={  2: {'position': [443.75925663230458, -186.13531854601777], 'userColor': None, 'useUserColor': False},
   3: {'position': [249.11810855050493, -264.33211369974435], 'userColor': None, 'useUserColor': False},
   4: {'position': [399.22484671837441, -262.6195983235753], 'userColor': None, 'useUserColor': False},
   5: {'position': [324.29994537344481, -188.141543144369], 'userColor': None, 'useUserColor': False},
   6: {'position': [247.23426028276998, -55.031231525218743], 'userColor': None, 'useUserColor': False},
   7: {'visualStyle': 1, 'position': [189.08679277147678, -321.8382870719139], 'color': None, 'text': u'(a) dataflow evaluation order', 'textColor': None, 'rectP2': (-1, -1)},
   8: {  'position': [350.13966757325443, -55.133765537235661],
         'useUserColor': False,
         'userColor': None},
   9: {'position': [350.77294679582781, -59.453041829801343], 'userColor': None, 'useUserColor': False},
   '__in__': {'position': [0, 0], 'userColor': None, 'useUserColor': True},
   '__out__': {'position': [0, 0], 'userColor': None, 'useUserColor': True}},
                             lazy=True,
                             eval_algo='LambdaEvaluation',
                             )




_89955408 = CompositeNodeFactory(name='evaluation order',
                             description='Explains in which order nodes evaluate in a dataflow',
                             category='tutorial',
                             doc='',
                             inputs=[],
                             outputs=[],
                             elt_factory={  5: ('openalea.python method', 'print'),
   9: ('openalea.file', 'expand_user_dir'),
   10: ('openalea.python method', 'range'),
   11: ('openalea.data structure', 'int'),
   12: ('openalea.data structure', 'int'),
   13: ('openalea.data structure', 'int'),
   14: ('openalea.flow control', 'annotation'),
   15: ('openalea.file.pickle', 'pickle dump'),
   16: ('openalea.file', 'filename')},
                             elt_connections={  10023228: (9, 0, 15, 1),
   10023240: (11, 0, 10, 0),
   10023252: (12, 0, 10, 1),
   10023264: (10, 0, 5, 0),
   10023276: (10, 0, 15, 0),
   10023288: (13, 0, 10, 2),
   10023300: (16, 0, 9, 0)},
                             elt_data={  5: {  'block': False,
         'caption': 'print',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x078CFCD0> : "print"',
         'hide': True,
         'id': 5,
         'lazy': False,
         'port_hide_changed': set(),
         'posx': -206.40436329982546,
         'posy': -468.12466299365218,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   9: {  'block': False,
         'caption': 'expand_user_dir',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x07869FD0> : "expand_user_dir"',
         'hide': True,
         'id': 9,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -465.01557323857111,
         'posy': -539.94428184158778,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   10: {  'block': False,
          'caption': 'Simulation',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x078CFC70> : "range"',
          'hide': True,
          'id': 10,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -225.38611854754262,
          'posy': -547.33091840106863,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   11: {  'block': False,
          'caption': '0',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x077BE510> : "int"',
          'hide': True,
          'id': 11,
          'lazy': False,
          'port_hide_changed': set(),
          'posx': -293.52827997763666,
          'posy': -621.67695865121095,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   12: {  'block': False,
          'caption': '6000',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x077BE510> : "int"',
          'hide': True,
          'id': 12,
          'lazy': False,
          'port_hide_changed': set(),
          'posx': -207.89690258310137,
          'posy': -619.50511490041981,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   13: {  'block': False,
          'caption': '2',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x077BE510> : "int"',
          'hide': True,
          'id': 13,
          'lazy': False,
          'port_hide_changed': set(),
          'posx': -99.265525188566073,
          'posy': -619.50511490041981,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   14: {  'factory': '<openalea.core.node.NodeFactory object at 0x07954870> : "annotation"',
          'id': 14,
          'posx': -325.69763320264155,
          'posy': -668.65023990927943,
          'txt': u'The "Simulation" node will run once, and\nafterwards only if any of its inputs changes.'},
   15: {  'block': False,
          'caption': 'pickleToDisk',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x074884F0> : "pickle dump"',
          'hide': True,
          'id': 15,
          'lazy': False,
          'port_hide_changed': set(),
          'posx': -453.18919748409405,
          'posy': -463.31144515628625,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   16: {  'block': False,
          'caption': 'filename',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x078AC0D0> : "filename"',
          'hide': True,
          'id': 16,
          'lazy': False,
          'port_hide_changed': set(),
          'posx': -443.85827125589617,
          'posy': -603.9087856982494,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   '__in__': {  'block': False,
                'caption': 'In',
                'delay': 0,
                'hide': True,
                'id': 0,
                'lazy': True,
                'port_hide_changed': set(),
                'posx': 0,
                'posy': 0,
                'priority': 0,
                'use_user_color': True,
                'user_application': None,
                'user_color': None},
   '__out__': {  'block': False,
                 'caption': 'Out',
                 'delay': 0,
                 'hide': True,
                 'id': 1,
                 'lazy': True,
                 'port_hide_changed': set(),
                 'posx': 0,
                 'posy': 0,
                 'priority': 0,
                 'use_user_color': True,
                 'user_application': None,
                 'user_color': None}},
                             elt_value={  5: [],
   9: [],
   10: [],
   11: [(0, '0')],
   12: [(0, '10000')],
   13: [(0, '2')],
   14: [],
   15: [(2, 'False')],
   16: [(0, "'~/simulationResults.txt'")],
   '__in__': [],
   '__out__': []},
                             elt_ad_hoc={  2: {  'position': [-288.83558778198534, -148.6420839916799],
         'useUserColor': False,
         'userColor': None},
   3: {  'position': [-450.77756285739429, -266.67241717137341],
         'useUserColor': False,
         'userColor': None},
   4: {  'position': [-300.67082468952481, -264.95990179520436],
         'useUserColor': False,
         'userColor': None},
   5: {  'position': [-206.40436329982546, -468.12466299365218],
         'useUserColor': False,
         'userColor': None},
   6: {  'position': [-375.5957260344544, -190.48184661599805],
         'useUserColor': False,
         'userColor': None},
   7: {  'position': [-452.66141112512923, -57.371534996847807],
         'useUserColor': False,
         'userColor': None},
   8: {  'color': None,
         'position': [-457.89567140789921, -328.34030347162906],
         'rectP2': (312.96656518014146, 329.60766390441859),
         'text': u'(c) block evaluation',
         'textColor': None},
   9: {  'position': [-465.01557323857111, -539.94428184158778],
         'useUserColor': False,
         'userColor': None},
   10: {  'position': [-225.38611854754262, -547.33091840106863],
          'useUserColor': False,
          'userColor': None},
   11: {  'position': [-293.52827997763666, -621.67695865121095],
          'useUserColor': False,
          'userColor': None},
   12: {  'position': [-207.89690258310137, -619.50511490041981],
          'useUserColor': False,
          'userColor': None},
   13: {  'position': [-99.265525188566073, -619.50511490041981],
          'useUserColor': False,
          'userColor': None},
   14: {  'color': None,
          'htmlText': u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n<html><head><meta name="qrichtext" content="1" /><style type="text/css">\np, li { white-space: pre-wrap; }\n</style></head><body style=" font-family:\'Sans\'; font-size:8pt; font-weight:400; font-style:normal;">\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">The &quot;Simulation&quot; node will run once, and</p>\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">afterwards only if any of its inputs changes.</p></body></html>',
          'position': [-325.69763320264155, -668.65023990927943],
          'rectP2': (-1, -1),
          'text': u'The "Simulation" node will run once, and\nafterwards only if any of its inputs changes.',
          'textColor': None,
          'visualStyle': 1},
   15: {  'position': [-453.18919748409405, -463.31144515628625],
          'useUserColor': False,
          'userColor': None},
   16: {  'position': [-443.85827125589617, -603.9087856982494],
          'useUserColor': False,
          'userColor': None},
   '__in__': {  'position': [0, 0], 'useUserColor': True, 'userColor': None},
   '__out__': {  'position': [0, 0], 'useUserColor': True, 'userColor': None}},
                             lazy=True,
                             eval_algo='LambdaEvaluation',
                             )




block = CompositeNodeFactory(name='block',
                             description='Usage of the block flag',
                             category='tutorial',
                             doc='',
                             inputs=[],
                             outputs=[],
                             elt_factory={  2: ('openalea.python method', 'print'),
   3: ('openalea.python method', 'range'),
   4: ('openalea.data structure', 'int'),
   5: ('openalea.data structure', 'int'),
   6: ('openalea.data structure', 'int'),
   7: ('openalea.flow control', 'annotation'),
   8: ('openalea.file.pickle', 'pickle dump'),
   9: ('openalea.file', 'filename'),
   10: ('openalea.file', 'expand_user_dir')},
                             elt_connections={  10023216: (10, 0, 8, 1),
   10023228: (9, 0, 10, 0),
   10023240: (3, 0, 8, 0),
   10023252: (5, 0, 3, 1),
   10023264: (6, 0, 3, 2),
   10023288: (3, 0, 2, 0),
   10023300: (4, 0, 3, 0)},
                             elt_data={  2: {  'block': False,
         'caption': 'print',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x078CFCD0> : "print"',
         'hide': True,
         'id': 2,
         'lazy': False,
         'port_hide_changed': set(),
         'posx': -309.70338857054657,
         'posy': -39.140781246044391,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   3: {  'block': True,
         'caption': 'Simulation',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x078CFC70> : "range"',
         'hide': True,
         'id': 3,
         'lazy': False,
         'port_hide_changed': set(),
         'posx': -328.68514381826373,
         'posy': -118.34703665346095,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   4: {  'block': False,
         'caption': '0',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x077BE510> : "int"',
         'hide': True,
         'id': 4,
         'lazy': False,
         'port_hide_changed': set(),
         'posx': -396.82730524835785,
         'posy': -192.69307690360318,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   5: {  'block': False,
         'caption': '10000',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x077BE510> : "int"',
         'hide': True,
         'id': 5,
         'lazy': False,
         'port_hide_changed': set(),
         'posx': -311.19592785382258,
         'posy': -190.52123315281204,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   6: {  'block': False,
         'caption': '2',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x077BE510> : "int"',
         'hide': True,
         'id': 6,
         'lazy': False,
         'port_hide_changed': set(),
         'posx': -202.56455045928726,
         'posy': -190.52123315281202,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   7: {  'factory': '<openalea.core.node.NodeFactory object at 0x07954870> : "annotation"',
         'id': 7,
         'posx': -428.99665847336274,
         'posy': -239.66635816167167,
         'txt': u'The "Simulation" node will run only once,\neven if its entries change.'},
   8: {  'block': False,
         'caption': 'pickleToDisk',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x074884F0> : "pickle dump"',
         'hide': True,
         'id': 8,
         'lazy': False,
         'port_hide_changed': set(),
         'posx': -556.4882227548153,
         'posy': -34.327563408678486,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   9: {  'block': False,
         'caption': 'filename',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x078AC0D0> : "filename"',
         'hide': True,
         'id': 9,
         'lazy': False,
         'port_hide_changed': set(),
         'posx': -547.78082365725345,
         'posy': -154.90855231774836,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   10: {  'block': False,
          'caption': 'expand_user_dir',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x07869FD0> : "expand_user_dir"',
          'hide': True,
          'id': 10,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -568.66529565811288,
          'posy': -101.01864363911348,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   '__in__': {  'block': False,
                'caption': 'In',
                'delay': 0,
                'hide': True,
                'id': 0,
                'lazy': True,
                'port_hide_changed': set(),
                'posx': 0,
                'posy': 0,
                'priority': 0,
                'use_user_color': True,
                'user_application': None,
                'user_color': None},
   '__out__': {  'block': False,
                 'caption': 'Out',
                 'delay': 0,
                 'hide': True,
                 'id': 1,
                 'lazy': True,
                 'port_hide_changed': set(),
                 'posx': 0,
                 'posy': 0,
                 'priority': 0,
                 'use_user_color': True,
                 'user_application': None,
                 'user_color': None}},
                             elt_value={  2: [],
   3: [],
   4: [(0, '0')],
   5: [(0, '10000')],
   6: [(0, '2')],
   7: [],
   8: [  (  1,
            "path(u'C:\\\\Documents and Settings\\\\barbeau/simulationResults.txt')"),
         (2, 'False')],
   9: [(0, "'~/simulationResults.txt'")],
   10: [],
   '__in__': [],
   '__out__': []},
                             elt_ad_hoc={  2: {  'position': [-309.70338857054657, -39.140781246044391],
         'useUserColor': False,
         'userColor': None},
   3: {  'position': [-328.68514381826373, -118.34703665346095],
         'useUserColor': False,
         'userColor': None},
   4: {  'position': [-396.82730524835785, -192.69307690360318],
         'useUserColor': False,
         'userColor': None},
   5: {  'position': [-311.19592785382258, -190.52123315281204],
         'useUserColor': False,
         'userColor': None},
   6: {  'position': [-202.56455045928726, -190.52123315281202],
         'useUserColor': False,
         'userColor': None},
   7: {  'color': None,
         'htmlText': u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n<html><head><meta name="qrichtext" content="1" /><style type="text/css">\np, li { white-space: pre-wrap; }\n</style></head><body style=" font-family:\'Sans\'; font-size:8pt; font-weight:400; font-style:normal;">\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">The &quot;Simulation&quot; node will run only once,</p>\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">even if its entries change.</p></body></html>',
         'position': [-428.99665847336274, -239.66635816167167],
         'rectP2': (-1, -1),
         'text': u'The "Simulation" node will run only once,\neven if its entries change.',
         'textColor': None,
         'visualStyle': 1},
   8: {  'position': [-556.4882227548153, -34.327563408678486],
         'useUserColor': False,
         'userColor': None},
   9: {  'position': [-547.78082365725345, -154.90855231774836],
         'useUserColor': False,
         'userColor': None},
   10: {  'position': [-568.66529565811288, -101.01864363911348],
          'useUserColor': False,
          'userColor': None},
   '__in__': {  'position': [0, 0], 'useUserColor': True, 'userColor': None},
   '__out__': {  'position': [0, 0], 'useUserColor': True, 'userColor': None}},
                             lazy=True,
                             eval_algo='LambdaEvaluation',
                             )




