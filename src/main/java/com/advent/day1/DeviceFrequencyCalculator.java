package com.advent.day1;

import com.advent.common.PuzzleInputReader;

import java.util.List;

import static com.advent.common.PuzzleInputReader.readInput;

public class DeviceFrequencyCalculator {
    public Integer calculateResultantFrequency() {
        return 10;
    }

    public Integer calculateResultantFrequency(String fileName) {
        List<String> puzzleInput =  PuzzleInputReader.readInput(fileName);
        Integer resultantFrequency = Integer.valueOf(puzzleInput.get(0));
        for (int i = 1; i < puzzleInput.size(); i++) {
            resultantFrequency += Integer.valueOf(puzzleInput.get(i));
        }
        return resultantFrequency;
    }
}
