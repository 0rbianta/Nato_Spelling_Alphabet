import json


class nac:
    def __init__(self, alphabet_path):
        self.alphabet = json.loads("{}")
        f = open(alphabet_path, "r")
        ob: str=None
        for i, w in enumerate(f.readlines()):
            w = w.replace("\n", "").lower()
            i += 1
            if i % 2 == 0:
                self.alphabet[ob] = w
            else:
                ob = w
        
        f.close()
    
    def text2nato(self, text):
        out = ""
        for i, char in enumerate(text):
            try:
                out += self.alphabet[char.lower()]
                if i != len(text) - 1:
                    out += " "
            except KeyError:
                pass
            except:
                pass
        return out

    def nato2text(self, text):
        out = ""
        for w in text.split(" "):
            try:
                out += w[0].lower()
            except KeyError:
                pass
            except IndexError:
                pass
            except:
                pass
        return out

def main():
    m_nac = nac("./ALPHABET.DAT")
    print(m_nac.text2nato("Hello World"))
    print(m_nac.text2nato("How are you"))
    print(m_nac.nato2text("hotel echo lima lima oscar whiskey oscar romeo lima delta"))


if __name__ == "__main__":
    main()
