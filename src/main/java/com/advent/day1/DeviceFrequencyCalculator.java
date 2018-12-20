package com.advent.day1;

import com.advent.common.PuzzleInputReader;

import java.util.List;

public class DeviceFrequencyCalculator {
    public Integer calculateResultantFrequency() {
        List<String> puzzleInput =  PuzzleInputReader.readPuzzleInput(1);
        return getFrequency(puzzleInput);
    }

    public Integer calculateResultantFrequency(String fileName) {
        List<String> puzzleInput =  PuzzleInputReader.readInput(fileName);
        return getFrequency(puzzleInput);
    }

    private Integer getFrequency(List<String> puzzleInput) {
        Integer resultantFrequency = Integer.valueOf(puzzleInput.get(0));
        for (int i = 1; i < puzzleInput.size(); i++) {
            resultantFrequency += Integer.valueOf(puzzleInput.get(i));
        }
        return resultantFrequency;
    }
}
