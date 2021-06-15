
# Collatz Conjecture
# 2k * n + 1 fail
# 5n + 1     fail
# n + 1      success
# 3n + 1     success

# def op(n):
#   if n % 2 == 0:
#     # print("%d / 2"%n)
#     return n / 2
#   else:
#     # print("3 x %d + 1"%n)
#     return 1 * n + 1

# def op(n):
#   if n % 3 == 0:
#     # print("%d / 3"%n)
#     return n / 3
#   elif n % 3 == 1:
#     # print("3 x %d + 1"%n)
#     return 1 * n + 2
#   else:
#     return 3 * n + 1

# types = []
# current_type = [1,1,1,1]
class Collatz:
  def __init__(self) -> None:
    self.current_type = []

  def op(self, n):
    r = n % 5
    if r == 1:
      return self.current_type[3] * n + 4
    elif r == 2:
      return self.current_type[2] * n + 3
    elif r == 3:
      return self.current_type[1] * n + 2
    elif r == 4:
      return self.current_type[0] * n + 1
    return n / 5

  def loop(self, n):
    r = self.op(n)
    if r == 1:
      return True
    return self.loop(r)

  def start(self, num):
    print(self.current_type)
    for i in range(2, num):
      # print(i)
      if self.loop(i):
        continue
      print(i, loop(i))
    print("all done, end to: " + str(num))

  # def start_diff_type(num):
  #   [int(x) for x in bin(16)[2:]]
  #   for idx in range(0, 15):
  #     origin_bins = [int(x) for x in bin(idx)[2:]]
  #     type = []
  #     for t in origin_bins:
  #       if t == 0:
  #         type.append(1)
  #       else:
  #         type.append(3)
  #     current_type = type
  #     print(current_type)
  #     start(num)

  def start_diff_type(self, num):
    types = [
      # [1, 1, 1, 1],
      # [1, 1, 1, 3],
      # [1, 3, 1, 3],
      # [3, 1, 1, 1],
      # [3, 1, 1, 3],
      [5, 1, 1, 1],
      # [3, 1, 3, 3],
      # [3, 3, 1, 1],
      # [3, 3, 1, 3],
      # [3, 3, 3, 1],
      # [3, 3, 3, 3],
      # [7, 5, 3, 1],
      # [7, 7, 7, 7],
      # [7, 5, 5, 5],
      # [7, 7, 7, 7],
      # [1, 7, 7, 7],
      # [3, 7, 7, 7],
    ]
    for i in range(len(types)):
      self.current_type = types[i]
      # print(self.current_type)
      self.start(num)

# start(1000000)
# loop(5)
Collatz().start_diff_type(1000000)
