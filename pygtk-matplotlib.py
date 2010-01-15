#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vi:ts=4 sw=4 et

# Code roughly based on:
# http://www.serpia.org/blog/2007/nov/03/matplotlib-and-pygtk-app/


import sys
import matplotlib
matplotlib.use('GTK')
from matplotlib.figure import Figure
from matplotlib.axes import Subplot
from matplotlib.backends.backend_gtk import FigureCanvasGTK
from numpy import arange, sin, pi


try:
    import pygtk
    pygtk.require("2.0")
except:
    pass
try:
    import gtk
    import gtk.glade
except:
    sys.exit(1)


class AppGui(object):
    def __init__(self):
        gladefile = "pygtk-matplotlib.glade"
        self.windowname = "main_window"
        self.wTree = gtk.glade.XML(gladefile, self.windowname)
        dic = {
            "on_main_window_destroy" : gtk.main_quit,
            "on_button1_clicked" : self.render_graph,
            #"on_button3_clicked" : self.fillTree,
            #"on_notebook1_switch_page" : self.selectNotebookPage,
            #"on_treeview1_button_press_event" : self.clickTree,
            #"on_button2_clicked" : self.createProjectGraph,
        }
        self.wTree.signal_autoconnect(dic)

        # setup matplotlib stuff on first notebook page (empty graph)
        self.figure = Figure(figsize=(6,4), dpi=72)
        self.axis = self.figure.add_subplot(1,1,1)
        self.axis.set_xlabel('Yepper')
        self.axis.set_ylabel('Flabber')
        self.axis.set_title('An Empty Graph')
        self.axis.grid(True)
        self.canvas = FigureCanvasGTK(self.figure) # a gtk.DrawingArea
        self.canvas.show()
        # Adding matplotlib canvas to our window
        self.graphview = self.wTree.get_widget("main_vbox")
        self.graphview.pack_start(self.canvas, True, True)

        #self.listview = self.wTree.get_widget("treeview1")
        #self.listmodel = gtk.ListStore(str, int, int, str, str)
        #self.listview.set_model(self.listmodel)
        #renderer = gtk.CellRendererText()
        #column = gtk.TreeViewColumn("Name",renderer, text=0)
        #column.set_clickable(True)
        #column.set_sort_column_id(0)
        #column.connect("clicked", self.createDBGraph)
        #column.set_resizable(True)
        #self.listview.append_column(column)

        self.wTree.get_widget(self.windowname).show()

    def render_graph(self, widget):
        print "render_graph()"
        self.axis.clear()

        self.axis.set_xlabel('Samples (n)')
        self.axis.set_ylabel('Value (-)')
        self.axis.set_title('Another Graph (click on the columnheader to sort)')
        self.axis.grid(True)

        # get columns from listmodel
        #age = []
        #for row in self.listmodel:
        #    age.append(row[1])
        #size = []
        #for row in self.listmodel:
        #    size.append(row[2])

        # get number of rows
        #N = len(age)
        #ind = arange(N) # the x locations for the groups
        #width = 0.35 # the width of the bars

        #p1 = self.axis.bar(ind, age, width, color='b')
        #p2 = self.axis.bar(ind+width, size, width, color='r')


        # destroy graph if it already exists
        #try:
        #    self.canvas2.destroy()
        #    break
        #except:
        #    print "nothing to destroy"
        #    break
        #self.canvas2 = FigureCanvasGTK(self.figure) # a gtk.DrawingArea
        #self.canvas2.show()
        #self.grahview = self.wTree.get_widget("vbox2")
        #self.grahview.pack_start(self.canvas2, True, True)


if __name__ == '__main__':
    main = AppGui()
    gtk.main()
