len_word = 0
        len_s = len(s)

        while len_s > 0:
            len_s -= 1
            if s[len_s] != " ":
                len_s += 1
            elif len_word > 0:
                return len_word 
                   
        return len_word