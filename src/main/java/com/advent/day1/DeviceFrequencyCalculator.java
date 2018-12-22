package com.advent.day1;

import com.advent.common.PuzzleInputReader;

import java.util.ArrayList;
import java.util.List;

class DeviceFrequencyCalculator {
    private final List<Frequency> dayOneInput =  PuzzleInputReader.readPuzzleInput(1);

    Frequency getResultantFrequency() {
        return calculateResultantFrequency(dayOneInput);
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

    public Frequency getFirstDuplicateFrequency() {
        return calculateFirstDuplicateFrequency(dayOneInput);
    }

    public Frequency getFirstDupicateFrequency(String fileName) {
        List<Frequency> puzzleInput = PuzzleInputReader.readInputAsFrequency(fileName);
        return calculateFirstDuplicateFrequency(puzzleInput);
    }

    private Frequency calculateFirstDuplicateFrequency(List<Frequency> puzzleInput) {
        List<Integer> resultantFrequencies = new ArrayList<>();
        Integer resultant = 0;
        boolean foundDuplicate = false;
        int counter = 0;
        while (!foundDuplicate) {
            resultantFrequencies.add(resultant);
            resultant += puzzleInput.get(counter).getValue();
            //System.out.println("R:" + resultant + ", V:" + puzzleInput.get(counter).getValue() + ", I:" + counter);
            if (resultantFrequencies.contains(resultant)) {
                foundDuplicate = true;
            }

            counter++;

            if (counter == puzzleInput.size()) {
                //System.out.println("Resetting Counter!");
                counter = 0;
            }
        }
        return new Frequency(resultant);
    }
}
