import hashlib


def crack_sha1_hash(hash, use_salts = None):
  salts = []
  fil1 = open('top-10000-passwords.txt', 'r', encoding='utf-8')
  fil2 = open('known-salts.txt', 'r', encoding='utf-8')
  
  Lines2 = fil2.readlines()
  for i in Lines2:
    salts.append(i)
  fil2.close()
  Lines = fil1.readlines()
  
  for line in Lines:
    for salt in salts:
      line.replace("\n", "")
      l = line.strip()
      if(use_salts):
        l2 = salt.strip() + l
        l3 = l + salt.strip()
        h2 = hashlib.sha1(l2.encode('utf-8'))
        h3 = hashlib.sha1(l3.encode('utf-8'))
        if(h2.hexdigest() == hash or h3.hexdigest() == hash):
          fil1.close()
          return line.strip()

      else:
        h = hashlib.sha1(l.encode('utf-8'))
        if(h.hexdigest() == hash):
          fil1.close()
          #print(hash)
          return line.strip()
  fil1.close()
  return "PASSWORD NOT IN DATABASE"
    