 
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    word_count1 = 0
    word_count2 = 0
    sticker_count1 = 0
    sticker_count2 = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == '王彥貿':
            for msg in s[2:]:
                if s[2] == '貼圖':
                    sticker_count1 += 1
                else:
                    word_count1 += len(msg)
        elif name == 'Jeff_Lu':
            for msg in s[2:]:
                if s[2] == '貼圖':
                    sticker_count2 += 1
                else:
                    word_count2 += len(msg)
    print('王彥貿說了', word_count1, '傳了', sticker_count1, '個貼圖')
    print('Jeff_Lu說了', word_count2, '傳了', sticker_count2, '個貼圖')
        #print(line)

def write_file(filename,chat):
    with open (filename, 'w', encoding = 'utf-8') as f:
        for p in chat:
            f.write(p + '\n')

def main():
    lines = read_file('[LINE]王彥貿.txt')
    convert(lines)
    #print(chat)
    #write_file('output.txt', chat)




main()