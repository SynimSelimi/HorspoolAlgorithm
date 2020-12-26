def shift_table(pattern): 
  sh_table = dict()
  pattern_len = len(pattern) - 1
  for i in range(0, pattern_len): 
    sh_table[pattern[i]] = pattern_len - i 
  return sh_table

def horspool_search(text, pattern): 
  sh_table = shift_table(pattern)
  ptrn_len = len(pattern)
  i = len(pattern) - 1

  while i <= len(text) - 1:
    matches = 0
    is_a_match = pattern[ptrn_len - 1 - matches] == text[i - matches]
    while matches < ptrn_len and is_a_match:
      is_a_match = pattern[ptrn_len - 1 - matches] == text[i - matches]
      matches += 1
    if matches == ptrn_len:
      return i - matches + 1
    else:
      offset = sh_table.get(text[i]) or ptrn_len
      i += offset
  return -1

def main():
  print("[+] Horspool Algorithm Demo")
  
  text = input("Enter message: ").strip()
  pattern = input("Enter pattern: ").strip()
  
  print(f'\n[+] Searching for "{pattern}" in message...')
  
  position = horspool_search(text, pattern)

  print((f'Found at {position}' if position != -1 else "Not Found"))
  if position != -1:
    ptrn_len = len(pattern)
    print(f'...{text[position - ptrn_len - 10:position + ptrn_len + 10]}...')

if __name__ == "__main__":
  main()