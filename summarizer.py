#a python implementation of a summarization algorithm i wrote for my app
#https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewSoftware?id=962626932
#translated from c++ to python so it still needs to be optimized for python
#many of the functions I had to write are already implemented
import json #needed for building the returnable json object
#words to not count as important
stopwords= "to into a about above after again against all am an and any are aren't as at be because been before being below between both but by can't cannot could couldn't did didn't do does doesn't doing don't down during each few for from further had hadn't has hasn't have haven't having he he'd he'll he's her here here's hers herself him himself his how how's i i'd i'll i'm i've if in into is isn't it it's its itself let's me more most mustn't my myself no nor not of off on once only or other ought our ours ourselves out over own same shan't she she'd she'll she's should shouldn't so some such than that that's the their theirs them themselves then there there's these they they'd they'll they're they've this those through to too under until up very was wasn't we we'd we'll we're we've were weren't what what's when when's where where's which while who who's whom why why's with won't would wouldn't you you'd you'll you're you've your yours yourself yourselves a able about above abst accordance according accordingly across act actually added adj affected affecting affects after afterwards again against ah all almost alone along already also although always am among amongst an and announce another any anybody anyhow anymore anyone anything anyway anyways anywhere apparently approximately are aren arent arise around as aside ask asking at auth available away awfully b back be became because become becomes becoming been before beforehand begin beginning beginnings begins behind being believe below beside besides between beyond biol both brief briefly but by c ca came can cannot can't cause causes certain certainly co com come comes contain containing contains could couldnt d date did didn't different do does doesn't doing done don't down downwards due during e each ed edu effect eg eight eighty either else elsewhere end ending enough especially et et-al etc even ever every everybody everyone everything everywhere ex except f far few ff fifth first five fix followed following follows for former formerly forth found four from further furthermore g gave get gets getting give given gives giving go goes gone got gotten h had happens hardly has hasn't have haven't having he hed hence her here hereafter hereby herein heres hereupon hers herself hes hi hid him himself his hither home how howbeit however hundred i id ie if i'll im immediate immediately importance important in inc indeed index information instead into invention inward is isn't it itd it'll its itself i've j just k keep keeps kept kg km know known knows l largely last lately later latter latterly least less lest let lets like liked likely line little 'll look looking looks ltd m made mainly make makes many may maybe me mean means meantime meanwhile merely mg might million miss ml more moreover most mostly mr mrs much mug must my myself n na name namely nay nd near nearly necessarily necessary need needs neither never nevertheless new next nine ninety no nobody non none nonetheless noone nor normally nos not noted nothing now nowhere o obtain obtained obviously of off often oh ok okay old omitted on once one ones only onto or ord other others otherwise ought our ours ourselves out outside over overall owing own p page pages part particular particularly past per perhaps placed please plus poorly possible possibly potentially pp predominantly present previously primarily probably promptly proud provides put q que quickly quite qv r ran rather rd re readily really recent recently ref refs regarding regardless regards related relatively research respectively resulted resulting results right run s said same saw say saying says sec section see seeing seem seemed seeming seems seen self selves sent seven several shall she shed she'll shes should shouldn't show showed shown showns shows significant significantly similar similarly since six slightly so some somebody somehow someone somethan something sometime sometimes somewhat somewhere soon sorry specifically specified specify specifying still stop strongly sub substantially successfully such sufficiently suggest sup sure a's able about above according accordingly across actually after afterwards again against ain't all allow allows almost alone along already also although always am among amongst an and another any anybody anyhow anyone anything anyway anyways anywhere apart appear appreciate appropriate are aren't around as aside ask asking associated at available away awfully be became because become becomes becoming been before beforehand behind being believe below beside besides best better between beyond both brief but by c'mon c's came can can't cannot cant cause causes certain certainly changes clearly co com come comes concerning consequently consider considering contain containing contains corresponding could couldn't course currently definitely described despite did didn't different do does doesn't doing don't done down downwards during each edu eg eight either else elsewhere enough entirely especially et etc even ever every everybody everyone everything everywhere ex exactly example except far few fifth first five followed following follows for former formerly forth four from further furthermore get gets getting given gives go goes going gone got gotten greetings had hadn't happens hardly has hasn't have haven't having he he's hello help hence her here here's hereafter hereby herein hereupon hers herself hi him himself his hither hopefully how howbeit however i'd i'll i'm i've ie if ignored immediate in inasmuch inc indeed indicate indicated indicates inner insofar instead into inward is isn't it it'd it'll it's its itself just keep keeps kept know known knows last lately later latter latterly least less lest let let's like liked likely little look looking looks ltd mainly many may maybe me mean meanwhile merely might more moreover most mostly much must my myself name namely nd near nearly necessary need needs neither never nevertheless new next nine no nobody non none noone nor normally not nothing novel now nowhere obviously of off often oh ok okay old on once one ones only onto or other others otherwise ought our ours ourselves out outside over overall own particular particularly per perhaps placed please plus possible presumably probably provides que quite qv rather rd re really reasonably regarding regardless regards relatively respectively right said same saw say saying says second secondly see seeing seem seemed seeming seems seen self selves sensible sent serious seriously seven several shall she should shouldn't since six so some somebody somehow someone something sometime sometimes somewhat somewhere soon sorry specified specify specifying still sub such sup sure t's take taken tell tends th than thank thanks thanx that that's thats the their theirs them themselves then thence there there's thereafter thereby therefore therein theres thereupon these they they'd they'll they're they've think third this thorough thoroughly those though three through throughout thru thus to together too took toward towards tried tries truly try trying twice two un under unfortunately unless unlikely until unto up upon us use used useful uses using usually value various very via viz vs want wants was wasn't way we we'd we'll we're we've welcome well went were weren't what what's whatever when whence whenever where where's whereafter whereas whereby wherein whereupon wherever whether which while whither who who's whoever whole whom whose why will willing wish with within without won't wonder would wouldn't yes yet you you'd you'll you're you've your yours yourself yourselves zero and or if of for the a as to is that in then you so as on our it your its more but objects can are when from by we be this that has had in to into all will with his which even at one an there about these us have where like just up them through been most also any widely"
#characters that can be left in the sentence
REGEX="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890/_- ";
#get an array from the stopwords
stopWordsArray=stopwords.split(' ')


def ksplit(string):
    array=[]
    tempStr=""
    for i in string:
        tempStr+=i
        if i == '.' or i=='?' or i=='!':
           # print tempStr
            array.append(tempStr)
            tempStr=""
    return array



#class to represent a node in a linked list of words
class Node(object):
    word = ""#represents the word
    count = 0#how many times the word appears
    link = None#link to next node
    def __init__(self, word=None, count=None, nextNode=None):#initialize the node
        if word!= None:
            self.word=word
        else:
            self.word=""
        if count !=None:
            self.count=count
        else:
            self.count=0
        if nextNode !=None:
            self.link=nextNode
       
#class to represent a node in a linked list of sentences


class Sentence(object):
    sentenceText = ""#what we do operations on
    punctuatedText= ""#what user will see
    headWord=None#head of list of words in the sentence
    sentenceScore = 0#score of all the words in the sentence
    link = None#next node
    def __init__(self, sentenceText=None, punctuatedText=None, headWord=None, sentenceScore=None, link=None):#initialize the node
    
        self.sentenceText = ""#sentenceText
        self.punctuatedText = ""#punctuatedText
        self.headWord = headWord
        self.sentenceScore = 0#sentenceScore
        self.link = link

    def __exit__(self):#delete the list
        os.unlink(self.sentenceText)
        os.unlink(self.punctuatedText)
        os.unlink(self.headWord)
        os.unlink(self.sentenceScore)
        os.unlink(self.link)

#linked list of words
class NodeList(object):
    #head of the list of nodes
    def __init__(self, head=None):#initialize the list
        if head == None:
            self.head=Node()
        else:
            self.head=head
        self.count=0

    def getCount(self):#get count of all the nodes
        temp=Node()
        temp=self.head
        count=0
        while temp != None:
            temp=temp.link
            count+=1
        return count

#linked list of sentences
class SentenceList(object):
    head=None
    def __init__(self, head=None):
        self.head=head

    def getCount(self):#get count of nodes in the list
        temp=Sentence()
        temp=self.head
        count=0
        while temp != None:
            temp=temp.link
            count+=1
        return count


#summarizes the text
#TODO: optimize for python and clean up
class Summarizer(object):

    summarizeHead=NodeList()#list of words
    newWords=NodeList()#list of words

    #check if the word is in the stopwords array
    def isUnimportant(self,wordToCheck):
        #print wordToCheck
        for i in stopWordsArray:
            #print i
           # print word
            if i == wordToCheck:
               # print word
                return True
            
        return False


    #print the nodes in the list, used for testing
    def recursivePrint(self,head, temp):
        if(temp.link==None):
            if temp.word=="":
                return
        else:
            if temp.word=="":
                temp=temp.link
                self.recursivePrint(self,head, temp)
            else:
                print temp.word
                temp=temp.link
                self.recursivePrint(head, temp)



    #create a new node with the given data
    def createNode(self,data):
        newNode=Node()
        newNode.word=data
        newNode.link=None
        newNode.count=0
        return newNode
    #add a node to the end of the list with the given data
    def addEndNode(self,head, data):
        temp=Node()
        temp=head
        while temp.link != None:
            temp=temp.link
        endN=Node()
        endN.word=data
        temp.link=endN

    #get to the end and append
    def recursiveFindNode(self,temp, toCopy):
        while temp.link!= None:
            temp=temp.link
        temp.link=toCopy

    #find the end of the list and append the given data
    def recursiveFind(self,temp, data):
        nTemp=Node()
        nTemp=temp
        while nTemp.link != None:
            nTemp=nTemp.link
        newNode=Node()
        newNode.word=data
        newNode.count=0
        nTemp.link=newNode

    #add a node to the end
    def addCopyEndNode(self,head, copy):
        temp=Node()
        temp=head
        while temp.link != None:
            temp=temp.link
        temp.link=copy

        #delete the list
    def deleteList(self,head):
        temp=Node()
        while head.link != None:
            temp=head
            head=head.link
            del head
        head.link = None()

    #copy one list to the other
    def copyList(self,listToCopyHead, copyListHead):
        self.deleteList(self.summarizeHead.head)
        self.summarizeHead.head=Node()
        self.summarizeHead.head.link=None
        temp=Node()
        temp=listToCopyHead
        while True:
            cpNode=Node()
            cpNode.word=temp.word
            cpNode.count=temp.count
            if cpNode.word != "" :
                self.addCopyEndNode(self.summarizeHead.head, cpNode)
            temp=temp.link
            if temp.link == None:
                break;

    #convert newline to space
    def newlineToSpace(self,input):
        fixed = input.replace('\n', ' ')
        return fixed


    #get the number of words in the document
    def getWordCount(self,input):
        arr=input.split(" ")
        words=arr.count
        return words

        #split the text based on the number of words
    def split(self,input, count):
        head=Node()
        arr=input.split()
        for i in arr:
            #print i
            self.addEndNode(head, i)
       # temp=Node()
        temp=head
        while temp.link != None:
            #print temp.word
            temp=temp.link
        return head

    #match every character in the text to the regex chars string
    def regexMatch(self,input):
        edited = ""
       # for c in input:
        #    for t in REGEX:
        #        if c==t and t != '.':
       #             edited += c
        edited=input
        return edited
    #lower case the input
    def lowerCase(self,input):
        return input.lower()

    #cut the list at the index and insert a node
    def splice(self,head, index, toCopyNode):
        temp = Node()
        temp = head
        for i in index-1:
            temp=temp.link
        toCopyNode.link=temp.link
        temp.link=toCopyNode

    #create a new sentence node with the given data
    def createSentenceNode(self,sentenceToCopy):
        sent = Sentence()
        sent.link=None
        sent.sentenceScore=0
        sent.sentenceText=sentenceToCopy
        sent.punctuatedText=""
        sent.headWord= None
        return sent
    #add a sentence node to the end of the list
    def addSentenceNode(self,head, data):
        temp= Sentence()
        temp = head
        while temp.link != None:
            temp=temp.link
        newSent = Sentence()
        newSent.sentenceText=data
        temp.link=newSent
    #get the sentences in the text
    def getSentences(self,text):#problem
        head=Sentence()
        count = 0
        temp=' '
        tempSentence=""
        size = len(text)
        #arr=text.split('.' or '!' or '?')
        arr=ksplit(text)
        for i in arr:
            #print i
            self.addSentenceNode(head, i)
        return arr

    #get the words in a sentence into a linked list
    def getWordsToNode(self,sent):
        tempSentence=sent.sentenceText
        #print tempSentence
        wordCount=self.getWordCount(tempSentence)
        #print wordCount
        head=Node()
        arr=tempSentence.split()
        for i in arr:
            #print i
            self.addEndNode(head, i)
        tempN=Node()
        tempN=head
        while tempN.link != None:
          #  print tempN.word
            tempN=tempN.link
        tempWord=Node()
        tempWord=head
        totalScore = 0
        sumTemp=Node()
        sumTemp=self.newWords.head
        while sumTemp.link != None:
            while tempWord.link != None:
               # print tempWord.word
              #  print sumTemp.word
                if tempWord.word== sumTemp.word and tempWord.word != "":
                   # print tempWord.word
                   # print tempWord.count
                    tempWord.count = sumTemp.count
                    totalScore+=sumTemp.count
                tempWord=tempWord.link
            if tempWord.word == sumTemp.word and tempWord.word != "":
                tempWord.count = sumTemp.count
                totalScore != sumTemp.count
            tempWord=head
            sumTemp=sumTemp.link
        
        while tempWord.link != None:
            tempWord=tempWord.link
        if tempWord.word == sumTemp.word and tempWord.word != "":
            tempWord.count=sumTemp.count
            totalScore+=sumTemp.count
        sent.headWord=head
        sent.sentenceScore=totalScore
    
        

    #get the words into a linked list for every sentence
    def assembleSentenceStruct(self,head):
        temp=Sentence()
        temp=head
        while temp.link != None:
            self.getWordsToNode(temp)
            temp=temp.link


    #swap sentences and and b
    def swap(self,a,b):
        temp=Sentence()
        temp.headWord=a.headWord
        temp.sentenceScore=a.sentenceScore
        temp.sentenceText=a.sentenceText
        temp.punctuatedText=a.punctuatedText

        a.headWord=b.headWord
        a.sentenceScore=b.sentenceScore
        a.sentenceText=b.sentenceText
        a.punctuatedText=b.punctuatedText

        b.headWord=temp.headWord
        b.sentenceScore=temp.sentenceScore
        b.sentenceText=temp.sentenceText
        b.punctuatedText=temp.punctuatedText
    #swap nodes a and b
    def swapNode(self,a,b):
        temp=Node()
        temp.word=a.word
        temp.count = a.count

        a.word=b.word
        a.count=b.count

        b.word=temp.word
        b.count=temp.count
    #organize the sentences based on total score
    def organizeScore(self,head):
        unsorted=True
        tempNode=Sentence()
        nextS=Sentence()
        while unsorted:
            tempNode=head
            unsorted=False
            while tempNode != None:
                nextS=tempNode
                nextS=nextS.link
                if nextS != None:
                    if nextS.sentenceScore >tempNode.sentenceScore:
                        self.swap(tempNode, nextS)
                        unsorted=True
                tempNode=tempNode.link
    #sort the words in order of score
    def organizeWordScore(self,head):
        unsorted=True
        tempNode=Node()
        nextW=Node()
        while unsorted:
            tempNode=head
            unsorted=False
            while tempNode != None:
                nextW=tempNode
                nextW=nextW.link
                if nextW != None:
                    if nextW.count > tempNode.count:
                        self.swapNode(tempNode, nextW)
                        unsorted=True
                tempNode=tempNode.link

    #summarize the text
    def summarize(self,text):
        self.summarizeHead=NodeList()
        self.newWords=NodeList()
        copyText=self.lowerCase(text)
        copyText+=(". . ")
        #print copyText
        copyText=self.regexMatch(copyText)
        #print copyText
        wordCount=self.getWordCount(copyText)
        self.summarizeHead.head=self.split(copyText, wordCount)
        temp=Node()
        temp=self.summarizeHead.head
        while temp.link != None:
           # print temp.word
            temp=temp.link
        sumTemp=Node()
        wordTemp=Node()
        added=False
        sumTemp=self.summarizeHead.head
        wordTemp=self.newWords.head
        #have one instance of a word total in the array
        while True:
            added=False
            while wordTemp.link != None:
                if wordTemp.word== sumTemp.word:
                    if wordTemp.word != "" and sumTemp.word != "":
                        added=True
                        break
                wordTemp=wordTemp.link
            if added==False and sumTemp.word != "":
                self.addEndNode(self.newWords.head, sumTemp.word)
            wordTemp=self.newWords.head
            sumTemp=sumTemp.link
            if sumTemp.link == None:
                break

        while wordTemp.link !=None:
            wordTemp=wordTemp.link
        if wordTemp.word ==sumTemp.word:
            if wordTemp.word != "" and sumTemp.word != "":
                added=True
            if added ==False and sumTemp.word != "":
                self.addEndNode(self.newWords.head, sumTemp.word)
        temp2=Node()
        temp2=self.newWords.head
        while temp2.link != None:
            #print temp2.word
            temp2=temp2.link
        sumTemp=Node()
        wordTemp=Node()
        sumTemp=self.summarizeHead.head
        wordTemp=self.newWords.head
        while sumTemp.link != None:
            while wordTemp.link!=None:
                if wordTemp.word == sumTemp.word:
                    if wordTemp.word != "" and sumTemp.word != "" and not self.isUnimportant(wordTemp.word):
                        wordTemp.count+=1
                        break
                wordTemp=wordTemp.link
                
            if wordTemp.link == None:
                if wordTemp.word == sumTemp.word:
                    if wordTemp.word != "" and sumTemp.word != "" and not self.isUnimportant(wordTemp.word):
                        wordTemp.count+=1
            wordTemp=self.newWords.head
            sumTemp=sumTemp.link
        while wordTemp.link != None:
            wordTemp=wordTemp.link
        if wordTemp.word == sumTemp.word:
            if wordTemp.word != "" and sumTemp.word != "" and not self.isUnimportant(wordTemp.word):
                wordTemp.count+=1
        copy=text
        sentHead=SentenceList()
        arr=self.getSentences(copy)
        sentHead.head=Sentence()
        for i in arr:
            self.addSentenceNode(sentHead.head, i)
        temp=Sentence()
        temp=sentHead.head
        while temp.link != None:
            #print temp.sentenceText
            temp.punctuatedText=temp.sentenceText
           # print temp.punctuatedText
            temp.sentenceText=self.lowerCase(temp.sentenceText)
            temp.sentenceText=self.regexMatch(temp.sentenceText)
            temp=temp.link
       # print temp.sentenceText
        temp.punctuatedText=temp.sentenceText
        temp.sentenceText=self.lowerCase(temp.sentenceText)
        temp.sentenceText=self.regexMatch(temp.sentenceText)

        temp=sentHead.head

        while temp.link != None:
            self.getWordsToNode(temp)
            temp=temp.link
        self.getWordsToNode(temp)
        self.organizeScore(sentHead.head)
        self.organizeWordScore(self.newWords.head)
        return sentHead


def apply(input):
    
    json_in=json.loads(input)
    originalInput=json_in['text']
    summaryLengthPercentage=json_in['summaryLength']
    keyTermsWanted=json_in['keyTermsWanted']
    if keyTermsWanted:
        numberOfKeyTerms=json_in['numKeyTerms']
    
    sentences=SentenceList()
    s=Summarizer()
    sentences=s.summarize(originalInput)
    KeyTermsHead=NodeList()
    json_data={}
    
    if keyTermsWanted:
        if numberOfKeyTerms > s.newWords.getCount():
            numberOfKeyTerms=s.newWords.getCount()
        KeyTermsHead=s.newWords
        temp=Node()
        temp=KeyTermsHead.head
        count=0
        kt=[]
        while temp.link !=None and count < numberOfKeyTerms:
            kt.append(temp.word)
           # kt+=','
            count+=1
            temp=temp.link
        json_data['keyTerms']=kt
    sentLength=sentences.getCount()
    numSentences=sentLength*summaryLengthPercentage
    count2=0
    temp=Sentence()
    temp=sentences.head
    summary=[]
    
    while temp.link != None and count2<numSentences:
        summary.append(temp.punctuatedText)
        #summary += '\n'
        count2+=1
        temp=temp.link
    json_data['summary']=summary
    fin_data=json.dumps(json_data)
    return fin_data
