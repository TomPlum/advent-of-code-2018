package com.advent.day1;

import com.advent.common.PuzzleInputReader;

import java.util.List;

class DeviceFrequencyCalculator {
    Frequency calculateResultantFrequency() {
        List<String> puzzleInput =  PuzzleInputReader.readPuzzleInput(1);
        return getFrequency(puzzleInput);
    }

    Frequency calculateResultantFrequency(String fileName) {
        List<String> puzzleInput =  PuzzleInputReader.readInput(fileName);
        return getFrequency(puzzleInput);
    }

    private Frequency getFrequency(List<String> puzzleInput) {
        Integer resultantFrequency = Integer.valueOf(puzzleInput.get(0));
        for (int i = 1; i < puzzleInput.size(); i++) {
            resultantFrequency += Integer.valueOf(puzzleInput.get(i));
        }
        return new Frequency(resultantFrequency);
    }
}
