package com.advent.day1;

import com.advent.common.PuzzleInputReader;

import java.util.ArrayList;
import java.util.List;

class DeviceFrequencyCalculator {
    Frequency getResultantFrequency() {
        List<Frequency> puzzleInput =  PuzzleInputReader.readPuzzleInput(1);
        return calculateResultantFrequency(puzzleInput);
    }

    Frequency getResultantFrequency(String fileName) {
        List<Frequency> puzzleInput =  PuzzleInputReader.readInputAsFrequency(fileName);
        return calculateResultantFrequency(puzzleInput);
    }

    private Frequency calculateResultantFrequency(List<Frequency> puzzleInput) {
        int resultantFrequency = puzzleInput.get(0).getValue();
        for (int i = 1; i < puzzleInput.size(); i++) {
            resultantFrequency += puzzleInput.get(i).getValue();
        }
        return new Frequency(resultantFrequency);
    }

    public Frequency calculateFirstDuplicateFrequency(String fileName) {
        List<Frequency> puzzleInput = PuzzleInputReader.readInputAsFrequency(fileName);
        List<Integer> resultantFrequencies = new ArrayList<>();
        Integer currentFrequency = puzzleInput.get(0).getValue();
        boolean foundDuplicate = false;
        int counter = 1;
        while (!foundDuplicate) {
            currentFrequency += puzzleInput.get(counter).getValue();
            resultantFrequencies.add(currentFrequency);
            if (resultantFrequencies.contains(currentFrequency)) {
                foundDuplicate = true;
            }

            if (counter == puzzleInput.size()) {
                counter = 1;
            }

            counter++;
        }
        return new Frequency(currentFrequency);
    }
}
