
class BaseStrategy:
    """ Here I will lay out the params for a given strategy """

    # I can define a given basket of assets
    stocks = []


    def initialize(self,context):
        pass


    def handle_data(self,context, data):
        pass

    def _test_args(self):
        pass

    def analyze(self, context, perf):
        pass
