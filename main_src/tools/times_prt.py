import numpy as np
import os
import main_src.constants                         as constants
from   main_src.tools.tools                   import get_argv
from   main_src.tools.tools                   import make_ASC_raster
from main_src.main_classes.General            import *
import main_src.io_functions.prt                  as prt

prtTimes = get_argv(constants.PARAMETER_PRINT_TIME)

print prtTimes
print

if prtTimes :
  class TimesPrt():
    def __init__(self):


      self.fTimes = open(prtTimes,'r')
      self.outsubrid = 'prubeh'
      self.outsubrid1 = 'htotal'
      self.outsubrid2 = 'hsheet'
      self.outsubrid3 = 'hrill'
      os.makedirs(Globals.outdir+os.sep+self.outsubrid)
      os.makedirs(Globals.outdir+os.sep+self.outsubrid+os.sep+self.outsubrid1)
      os.makedirs(Globals.outdir+os.sep+self.outsubrid+os.sep+self.outsubrid2)
      os.makedirs(Globals.outdir+os.sep+self.outsubrid+os.sep+self.outsubrid3)
      self.times  = []
      self.__n    = 0

      for line in self.fTimes.readlines():
        z = line.split()
        if len(z) == 0:
          continue
        elif z[0].find('#') >= 0 :
          continue
        else:
          if len(z) == 0:
              continue
          else:
            self.times.append(float(line))
      self.times.sort()



    def prt(self,time,dt,sur):
      if self.__n == len(self.times) :
        return

      if (time < self.times[self.__n]) & (self.times[self.__n] <=time+dt) :

        cas = '%015.2f' % (time+dt)
        filen = Globals.outdir + os.sep  + self.outsubrid + os.sep  + self.outsubrid1 + os.sep+ 'H' + str(cas).replace('.','_')+'.asc'
        filen2 = Globals.outdir + os.sep  + self.outsubrid + os.sep  + self.outsubrid2 + os.sep+ 'h_sheet' + str(cas).replace('.','_')+'.asc'
        filen3 = Globals.outdir + os.sep  + self.outsubrid + os.sep  + self.outsubrid3 + os.sep+ 'h_rill' + str(cas).replace('.','_')+'.asc'
        prt.message("Printing total H into       file: ." +os.sep+ filen + '...')
        prt.message("Printing total h_sheet into file: ." +os.sep+ filen2 + '...')
        prt.message("Printing total h_rill  into file: ." +os.sep+ filen3 + '...')
        prt.message("-----------------------------------------------------------")
        prt.message("-----------------------------------------------------------")
        tmp =  np.zeros([Globals.r,Globals.c],float)

        for i in Globals.rr:
          for j in Globals.rc[i]:
            tmp[i][j] = sur.arr[i][j].h_total_new

        make_ASC_raster(filen,tmp,Globals)
        
        for i in Globals.rr:
          for j in Globals.rc[i]:
            tmp[i][j] = sur.arr[i][j].h_sheet

        make_ASC_raster(filen2,tmp,Globals)
        
        
        for i in Globals.rr:
          for j in Globals.rc[i]:
            tmp[i][j] = sur.arr[i][j].h_rill

        make_ASC_raster(filen3,tmp,Globals)


        # pro pripat, ze v dt by bylo vice pozadovanych tisku, v takovem pripade udela jen jeden
        # a skoci prvni cas, ktery je mimo
        while (time < self.times[self.__n]) & (self.times[self.__n] <=time+dt) == True :
          self.__n += 1
          if self.__n == len(self.times) :
            return






else:
  class TimesPrt():
    def __init__(self):
      pass

    def prt(self,time,dt,sur):
      pass