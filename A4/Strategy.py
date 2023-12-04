from abc import ABC, abstractmethod
from A4.Collection import Collection

class Strategy(ABC):
    @abstractmethod
    def execute(self):
        pass

class StrategyReadFromFile(Strategy):
    def execute(self, collection: Collection, log: str, filename: str,  pos: int):
        collection.read_from_file(filename, log, pos)

        

class StrategyReadFromConsole(Strategy):
    def execute(self, collection: Collection, log: str, filename: str,  pos: int):
        collection.add_element_console(log)

class Default(Strategy):
    def execute(self, collection: Collection, log: str, filename: str,  pos: int):
        print("Invalid strategy")

class InsertElement:
    strategy: Strategy

    def __init__(self, strategy: Strategy = None):
        if strategy is None:
            self.strategy = Default()
        else:
            self.strategy = strategy
    
    def setStrategy(self, strategy: Strategy):
        self.strategy = strategy

    def executeStrategy(self, collection: Collection, log: str = None, filename: str = None, pos: int = None):
        self.strategy.execute(collection, log, filename, pos)


        