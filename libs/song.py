## Object song

class chorus():
    def __init__(self):
        self.body = ""

    def content(self):
        return self.body

    def is_chorus(self):
        return True

class verse():
    def __init__(self):
        self.body = ""

    def content(self):
        return self.body

    def is_chorus(self):
        return False

class song():
    
    def __init__(self, newtitle, newbody=[], newmauthor = "Unknown", newtauthor="Unknown", newtone="Unknown", newyear="Unknown"):
        # Initialize vars..
        self.title = newtitle
        # Body is an array of string with verses and
        # chorus to be understood with __structure
        self.body = newbody
        
        self.mauthor = newmauthor
        self.tauthor = newtauthor
        self.tone = newtone
        self.year = newyear

        # Structure is an array of the type 'c' 'v'
        # where c means Chorus, v means Verse
        self.structure = []
    
    
    # Gives the number of chorus in the song
    def n_chorus(self):
        count = 0
        for item in self.structure:
            if(item == 'c'):
                count += 1
        return count
    
    # Gives the number of verse in the song
    def n_verse(self):
        count = 0
        for item in self.structure:
            if(item == 'v'):
                count += 1
        return count

    def is_chorus(self, n):
        if(self.structure[n] == 'c'):
            return 1
        return 0

    def is_verse(self, n):
        if(self.structure[n] == 'v'):
            return 1
        return 0

    def add_chorus(self, t_chorus):
        newchorus = chorus()
        newchorus.body = t_chorus
        self.body.append(newchorus)
        self.structure.append('c')

    def add_verse(self, t_verse):
        newverse = verse()
        newverse.body = t_verse
        self.body.append(newverse)
        self.structure.append('v')
