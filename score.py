class Score:
    """ Simple class to represent a score in a game """

    def __init__(self, name, score):
        """ Initializes private attributes

        Args:
            name (str): name of the player (cannot be empty)
            score (int): score of the player (cannot be negative)

        Raises:
            ValueError: name is empty or not string, score is not integer or negative
        """

        if type(name) is not str or not name:
            raise ValueError("Invalid name.")
        if type(score) is not int or score < 0:
            raise ValueError("Invalid score.")

        self._name = name
        self._score = score

    def __str__(self):
        """ Human readable form of our Score class instance

        Returns:
            str
        """
        return f"Score: {self._name} ({self._score})"

    def __lt__(self, other_score):
        """ Defines a less than dunder method for Score class 

        Args:
            other_score (obj)

        Raises:
            TypeError: other_score must be an isntance of Score

        Returns:
            bool
        """
        if type(other_score) is not type(self):
            raise TypeError
        return self._score < other_score._score

    def to_dict(self):
        """ Returns a dictionary representation of this score """
        return {"name": self._name, "score": self._value}
