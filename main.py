def shift_table(pattern): 
  sh_table = dict()
  pattern_len = len(pattern) - 1
  for i in range(0, pattern_len): 
    sh_table[pattern[i]] = pattern_len - i 
  return sh_table

def main():
  print("[+] Horspool Algorithm Demo")
  
  text = input("Enter message: ").strip()
  pattern = input("Enter pattern: ").strip()
  
  print(f'\n[+] Searching for "{pattern}" in message...')
  
  # position = horspool_search(text, pattern)
  position = -1
  sh_table = shift_table(pattern)
  print(sh_table)

  print((f'Found at {position}' if position != -1 else "Not Found"))

if __name__ == "__main__":
  main()