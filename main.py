samples = [{
  "text": "Nëse kërkesat e absurdit nuk respektohen në vepër, nëse ajo nuk ilustron divorcin dhe revoltën, nëse ajo u bën lëshime iluzioneve dhe ngjall shpresë, ajo nuk është më e padobi. Nuk mund të shkëputem më prej saj.",
  "pattern": "lëshime iluzioneve",
  "asserts": True
},
{
  "text": "Tani që kishte lënë prapa ditët e mërzitshme e të ftohta në mal dhe kishte veshur uniformën e re, po e kapte përsëri ndjenja e madhështisë. Fshatari kishte fytyrë të hequr dhe sy të përhimë.",
  "pattern": "përhimë?",
  "asserts": False
},
{
  "text": "Çdo njeri i dashuruar do t'i thotë të dashurës së tij: të dua, xhan, të dua dhe do t'i thotë se e dashuron në gjuhën e tij kombëtare, por do ta realizojë dashurinë me të brenda kushtesh të posaçme, specifike për mjedisin dhe popullin e tij.",
  "pattern": "kombëtare",
  "asserts": True
},
{
  "text": "Ata s'paskëshin qenë rapsodë, por magjistarë. Ujana e keqe rridhte ndërkaq mospërfillëse.",
  "pattern": "muzikë",
  "asserts": False
},
{
  "text": "Dhe këta heshtakë zakonisht heshtin vetëm publikisht, por veprojnë nën tokë: i sufrojnë të tjerët, u mbajnë ligjërata të fshehta, ua hartojnë strategjinë dhe, mandej, kapardisen për ngadhnjimin e një të bëre të caktuar.",
  "pattern": "veprojnë",
  "asserts": True
}]

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

    def is_match():
      return pattern[ptrn_len - 1 - matches] == text[i - matches]

    while matches < ptrn_len and is_match():
      matches += 1
    if matches == ptrn_len:
      return i - matches + 1
    else:
      offset = sh_table.get(text[i]) or ptrn_len
      i += offset
  return -1

def is_found(position):
  return True if position != -1 else False

def round_zero(nm):
  return 0 if nm < 0 else nm
  
def round_top(nm, top):
  return top if nm > top else nm

def print_result(position, text, pattern):
  print((f'Found "{pattern}" at {position}' if is_found(position) else "Not Found\n"))
  if position != -1:
    ptrn_len = len(pattern)
    begin = round_zero(position - ptrn_len - 10)
    end = round_top(position + ptrn_len + 10, len(text))
    print(f'... {text[begin:end]} ...\n')

def demo1():
  print("[+] Horspool Algorithm Demo 1")
  for sample in samples:
    position = horspool_search(sample['text'], sample['pattern'])
    print(f'Working properly? - {is_found(position) == sample["asserts"]}')
    print_result(position, sample['text'], sample['pattern'])

def demo2():
  print("[+] Horspool Algorithm Demo 2")
  
  text = input("Enter message: ").strip()
  pattern = input("Enter pattern: ").strip()
  
  print(f'\n[+] Searching for "{pattern}" in message...')
  
  position = horspool_search(text, pattern)

  print_result(position, text, pattern)

def main():
  demo1()
  demo2()

if __name__ == "__main__":
  main()