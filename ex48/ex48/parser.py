class ParserError(Exception):
	pass


class Sentence(object):

	def __init__(self, subject, verb, objecti, test):
		self.subject = subject[1]
		self.verb = verb[1]
		self.objecti = objecti[1]
        self.test = test[1]

class Parse(object):

    def __init__(self):
        pass

    def peek(self, word_list):
        """
        Returns the 'word type' of the first value in word_list
        If list is empty, returns None"""

        if word_list: #if tuple exists
            word = word_list[0] #looks at the first tuple
            return word[0] #returns the tuple
        else:
            return None


    def match(self, word_list, expecting):
        """
        pops the first tuple off the word list.
        If the tuple 'word type' matches expecting, it returns the
        tuple.
        If the tuple 'word type' does not match expecting, it returns None
        It will also return None when word_list is empty"""

        if word_list: #if list exists
            word = word_list.pop(0) #pop the first tuple of list

            if word[0] == expecting: # if it's the type of word you wanted
                return word # returns the tuple
            else:
                return None
        else:
            return None #if list is not populated


    def skip(self, word_list, word_type):
        """
        Checks first tuples in word_list if they have a 'word type'
        that matches word_type.
        The tuple 'word type' is popped off the list without returning.
        It continues until it runs into another word type.
        """
        while self.peek(word_list) == word_type:
            self.match(word_list, word_type)
            #While word list is populated with the word_type,
            #match the


    def parse_verb(self, word_list):
        self.skip(word_list, 'stop') #pops off any stop types in front
        self.skip(word_list, 'error')
        self.skip(word_list, 'number')

        if self.peek(word_list) == 'verb': #if verb is next
            return self.match(word_list, 'verb') #pops verb off and returns
        else:
            raise ParserError("Expected a verb next.")

    # def parse_number(self, word_list):
    #     """
    #     pops all stop words off front then returns a number
    #     """
    #     self.skip(word_list, 'stop')
    #     self.skip(word_list, 'error')
    #     next = self.peek(word_list)
    #
    #     if next == 'number':
    #         return self.match(word_list, 'number')
    #     else: #not using elif, so both can evaluate
    #         return None
    #     # else:
    #     #     raise ParserError("Expected a number or nothing next.")

    def parse_object(self, word_list):
        """
        pops all stop words off front then returns a noun and/or direction
        """
        self.skip(word_list, 'stop')
        self.skip(word_list, 'error')
        self.skip(word_list, 'number')
        next = self.peek(word_list)

        if next == 'noun':
            return self.match(word_list, 'noun')
        if next == 'direction': #not using elif, so both can evaluate
            return self.match(word_list, 'direction')
        else:
            raise ParserError("Expected a noun or direction next.")


    def parse_subject(self, word_list, subj):
        """
        Take the subject and word list.
        Parses for verbs and for an object"""
        verb = self.parse_verb(word_list)
        # numb = self.parse_number(word_list)
        obj = self.parse_object(word_list)
        test = ('test', 'test')

        return Sentence(subj, verb, obj, test) # builds sentence obj


    def parse_sentence(self, word_list):
        """
        > Skips stop types
        > takes the first tuple from the list
        > determines if it is a noun or verb
        > if it's a noun, it is the subject
        > if a verb, player is subject
        > passes the word list and subject into the other functions
        > First word is popped off if it is a noun"""
        self.skip(word_list, 'stop')


        start = self.peek(word_list)

        if start == 'noun':
            subj = self.match(word_list, 'noun')
            return self.parse_subject(word_list, subj)
        elif start == 'verb':
            # assume the subject is the player than
            return self.parse_subject(word_list, ('noun', 'player'))
        else:
            raise ParserError(("Must start with subject, object, or"
                              + " verb not: %s" % start))
