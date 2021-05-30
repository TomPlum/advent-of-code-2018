from dataclasses import dataclass


@dataclass
class Input:
    value: [str]

    def toString(self) -> [str]:
        return self.value

    def toInteger(self) -> [int]:
        return [int(numeric_string) for numeric_string in self.value]
