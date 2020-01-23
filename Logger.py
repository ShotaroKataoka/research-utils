import os
from glob import glob

class Logger():
  def __init__(self, logdir):
    self.logs = {}
    if logdir[-1]!="/": logdir+="/"
    self.logdir = logdir
    if not os.path.exists(logdir):
      os.mkdir(logdir)

  def set_title(self, title):
    self.title = title

  def add_log(self, key, value):
    if type(value)==type(""):
      assert "\n" not in value, "\\n can't be in log."
    self.logs[key] = value

  def save_log(self, delimiter=","):
    if not os.path.exists(self.logdir+self.title):
      os.mkdir(self.logdir+self.title)
    for i in range(10000):
      if not os.path.exists(self.logdir + self.title + f"/log-{i:0=4}.txt"):
        break
    filename = f"/log-{i:0=4}.txt"
    with open(self.logdir + self.title + filename, "w") as f:
      f.write(f"key{delimiter} log\n")
      for key, item in self.logs.items():
        f.write(f"{key}{delimiter} {item}\n")
    print(f"save log successfully.\n{self.logdir+filename}")
