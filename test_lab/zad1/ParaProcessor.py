class Process:
    @staticmethod
    def proc(args):
        """
        Function printing args
        :param args: should be a list or tuple
        :return:
        """
        for ind, val in enumerate(args):
            print ind, " parameter value is ", val
