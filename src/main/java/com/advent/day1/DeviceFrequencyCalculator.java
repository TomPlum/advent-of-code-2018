package com.advent.day1;

import com.advent.common.ListUtils;
import com.advent.common.PuzzleInputReader;
import com.advent.domain.Frequency;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.atomic.AtomicLong;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

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
        AtomicInteger resultant = new AtomicInteger(0);
        Stream<Integer> integerStream = puzzleInput.stream().map(Frequency::getValue);
        List<Integer> list = integerStream.sequential().mapToInt(resultant::addAndGet).boxed().collect(Collectors.toList());
        return new Frequency(ListUtils.getLastElement(list));
    }

    Frequency getFirstDuplicateFrequency() {
        return calculateFirstDuplicateFrequency(dayOneInput);
    }

    Frequency getFirstDuplicateFrequency(String fileName) {
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
