from score import Score


class ScoreManager:
    """ Simple class to manage a collection of scores

    Attributes:
        scores (list): the list of scores managed by the instance
    """

    def __init__(self):
        """ Initializes private attributes """
        self._scores = list()

    @property
    def scores(self):
        """ Get a score list by sorting the list by scores

        Returns:
            scores_list (list)
        """
        scores_list = []

        for score in sorted(self._scores, reverse=True):
            score_dict = {}
            score_dict["name"] = score._name
            score_dict["score"] = score._score
            scores_list.append(score_dict)
        return scores_list

    def add_score(self, score):
        """ Method: add a new score instance to ScoreManager

        Args:
            score (obj)

        Raises:
            TypeError: score must be in isntance of Score class
        """
        if type(score) is not Score:
            raise TypeError("Invalid score.")

        self._scores.append(score)

    def __len__(self):
        """ Defines len dunder method 

        Returns:
            int
        """
        return len(self._scores)

    def remove_user_score(self, user_name):
        """ Method: Removes a score instance from a list if the user_name matches

        Args:
            user_name ("str")
        """
        new_scores = list(filter(lambda x: x._name != user_name, self._scores))
        self._scores = new_scores

    #
