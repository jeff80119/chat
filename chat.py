 
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None
    for line in lines:
        if '李柏恩' in line:
            person = line
            continue
        elif 'Jeff Lu' in line:
            person = line
            continue
        elif new == []:
            new.append(line)
            continue
        elif person:
            new.append(person + ': ' + line)
            person = None
    return new

def write_file(filename,chat):
    with open (filename, 'w', encoding = 'utf-8') as f:
        for p in chat:
            f.write(p + '\n')

def main():
    lines = read_file('input.txt')
    chat = convert(lines)
    print(chat)
    write_file('output.txt', chat)




main()