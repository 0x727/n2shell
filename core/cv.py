import random,hashlib

def grs(randomlength=10):#https://blog.csdn.net/hefener/article/details/109725477 generate_random_str
  random_str = ''
  base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
  length = len(base_str) - 1
  for i in range(randomlength):
    random_str += base_str[random.randint(0, length)]
  return random_str

def cmd5(message):#https://blog.csdn.net/weixin_44799217/article/details/112486097 computeMD5
    m = hashlib.md5()
    m.update(message.encode(encoding='utf-8'))
    return m.hexdigest()