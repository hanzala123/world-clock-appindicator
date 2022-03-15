#!/usr/bin/python
import pytz
import os
import sys
import gi
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Gtk', '3.0')

from gi.repository import AppIndicator3 as appindicator
from gi.repository import Gtk as gtk
from gi.repository import GLib
from datetime import datetime

last_status = None

def get_timezones():
  timezones = []
  if os.path.exists("timezones.txt"):
    with open("timezones.txt") as f:
      all_tz = f.read().splitlines()
    
    for tz in all_tz:
      if not tz.startswith("#"):
        timezones.append(tz.strip())
    
    return timezones

  else:
    print("timezones.txt file does not exist. Run 'python3 get_tz.py' to generate the file.")
    print("Then remove the '#' from the timezone(s) you want to enable from the timezones.txt file.")
    quit()



def get_all_times():
  timezones = get_timezones()
  if not timezones:
    print("No Timezone selected.")
    print("Plese remove the '#' from beginning of the timezone(s) you want to enable from the timezones.txt file.")
    quit()

    
  times = []
  for timezone in timezones:
    tz = pytz.timezone(timezone)
    time = (datetime.now(tz))
    time_str = time.strftime("%H:%M")
    if time.strftime("%d/%m/%Y") != datetime.now().strftime("%d/%m/%Y"):
      time_str = time.strftime("%H:%M (%d/%m/%Y)")
    times.append(time_str + "  " + timezone.split("/")[-1])

  return times

def update_menu(indicator):
  global last_status
  all_times = get_all_times()
  if all_times == last_status:
    return True
  
  last_status = all_times

  menu = gtk.Menu()
  for t in all_times:
    item = gtk.MenuItem(label=t)
    menu.append(item)
    
  Separator = gtk.SeparatorMenuItem()
  menu.append(Separator)

  exittray = gtk.MenuItem(label='Quit')
  exittray.connect('activate', quit)
  menu.append(exittray)

  menu.show_all()
  indicator.set_menu(menu)
  return True # Without returning True GLib.timeout_add() will not continue 


def quit(_=None):
  gtk.main_quit()
  sys.exit()

if __name__ == "__main__":
  indicator = appindicator.Indicator.new("customtray", "gnome-clocks", appindicator.IndicatorCategory.APPLICATION_STATUS)
  indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
  GLib.timeout_add(1000, update_menu, indicator)
  gtk.main()