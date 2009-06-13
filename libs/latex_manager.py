import re

class latex_manager():
    def __init__(self):
        ## TODO: Verify Latex Installation
        return

    def create_song(self, song):
        # Ci aspettiamo di ottenere un oggetto song
        title = song.title
        tone = song.tone
        mauthor = song.mauthor
        tauthor = song.tauthor
        year = song.year
        body = song.body
        
        # We really have to assume that latex_song is unicode, 
        # or the write() function will eat us!
        latex_song = unicode()
        latex_song += "\\begin{song}{" + title + "}{" + tone + "}\n{" + mauthor + "}\n{" + tauthor + "}\n{" + year + "}" + "{}\n\n\\index{" + title + "}\n\n"

        for item in body:
            if(item.is_chorus()):
                latex_song += "\n\\begin{SBChorus}\n"
                latex_song += re.sub("\n", "\n\n", item.content())
                latex_song += "\n\\end{SBChorus}\n"
            else:
                latex_song += "\n\\begin{SBVerse}"
                latex_song += re.sub("\n" , "\n\n", item.content())
                latex_song += "\n\\end{SBVerse}\n"

        latex_song += "\n\\end{song}\n\n"
        
        # Transform chords in LaTeX Chords (this part has to be removed..)
        #latex_song = re.sub("\[", "\\Ch{", latex_song)
        #latex_song = re.sub("\](\w|\s){4}", self.quadra_to_chord_end, latex_song)
        #latex_song = re.sub("\]", "}{}", latex_song)

        latex_song = self.sub_chord(latex_song)
        
        return latex_song
        

    def sub_chord(self,m):
        j = 0
        # print j, len(m) this is just debug!
        while(j < len(m)):
            if(m[j] == '['):
                # We have a chord!, then...
                # 1) How many letters is the chords?
                count = 0
                while(m[count + j + 1] != ']'):
                    count += 1
                # 2) Are there count + 1 words "free" after the chord?
                free = count + 2
                for i in range(j + count + 2,j + count + 2 + (count + 2) ):
                    # print "m[i] = ", m[i] Removing debug
                    if( (m[i] == '\n') | (m[i] == '[') | (m[i] == '{') ):
                        free = i - j - count - 2
                        break
                # Debug is unuseful now! print "free = " , free
                # Free what we need...and rebuild the new string...
                m = m[0:j] + "\Ch{" + m[j+1:j+count+1] + "}{" + m[j+count+2:j+count+free+2] + "}" + m[j+count+free+2:len(m)]
                j = j + count + free + 3
            else:
                j += 1
        return m

    def export_songbook(self,song_list):
        # Assume that song list is an array of songs and
        # create a songbook with them

        # New buffer
        buf = unicode()

        # TODO: Latex code to compile the songbook
        # Document class
        buf += "\documentclass[10pt,a5paper,twoside]{book}\n"
        
        # Packages
        buf += "\usepackage[a5paper,chordbk]{songbook}\n"
        buf += "\usepackage[utf8x]{inputenc}\n"
        buf += "\usepackage{makeidx}\n"
        buf += "\n\n"

        # Index generation
        buf += "\MakeTitleIndex\n"
        buf += "\MakeTitleContents\n"
        buf += "\MakeKeyIndex\n"
        buf += "\makeindex\n"
        buf += "\n\n"

        # Document begins
        buf += "\\begin{document}\n\n"
        
        for song in song_list:
            buf += "\n\n" # Put some space between songs
            buf += "% Canzone:" + song.title + "\n\n"
            buf += self.create_song(song)

        # The Index
        buf += "\printindex\n"

        # Document ends
        buf += "\end{document}\n\n"
            
        # Give buffer back to be printed
        return buf
