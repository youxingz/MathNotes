import itertools

avaliable_multiplers = [1, 3]

class LoopCollatz:
  def __init__(self) -> None:
    self.size = 2
    self.arrangment = [1, 1]
    pass

  def operate(self, n):
    r = n % self.size
    if r == 0:
      return n / self.size
    else:
      print(n, self.arrangment[r - 1])
      return self.arrangment[r - 1] * n + (self.size - r)
  
  def loop(self, num):
    s = self.operate(num)
    if s == 1:
      return True
    return self.loop(s)

  def try_loop(self, num):
    try:
      return self.loop(num)
    except:
      return False

  def start_one_loop(self, start=2, end=100):
    for i in range(start, end):
      if not self.try_loop(i):
        # print('Fail')
        return False
    # print('Success')
    return True
  
  def start_all_loops(self, start=2, end=100):
    for size in range(2, 3):
      self.size = size
      # self.arrangment = []
      arrangments = []
      for it in range(size):
        arrangments.append(avaliable_multiplers)
      for arrangment in itertools.product(*arrangments):
        # print('current: ', arrangment)
        self.arrangment = arrangment
        # start one arrangment
        result = self.start_one_loop(start, end)
        if result:
          print('success: ', arrangment)
        else:
          # print('fail   : ', arrangment)
          pass

LoopCollatz().start_all_loops(2, 10)
