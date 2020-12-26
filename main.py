def main():
  print("[+] Horspool Algorithm Demo")
  
  text = input("Enter message: ").strip()
  pattern = input("Enter pattern: ").strip()
  
  print(f'\n[+] Searching for "{pattern}" in message...')
  
  # position = horspool_search(text, pattern)
  position = -1

  print((f'Found at {position}' if position != -1 else "Not Found"))

if __name__ == "__main__":
  main()