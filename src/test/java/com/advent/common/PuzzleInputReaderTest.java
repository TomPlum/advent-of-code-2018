package com.advent.common;

import org.junit.jupiter.api.Test;

import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;

class PuzzleInputReaderTest {
    @Test
    void readTestInput() {
        String fileName = "test-input.txt";
        List<String> result = PuzzleInputReader.readInput(fileName);
        assertThat(result.get(0)).isEqualTo("Hello World!");
    }

    @Test
    void readPuzzleInput() {
        Integer dayNumber = 1;
        List<String> result = PuzzleInputReader.readPuzzleInput(dayNumber);
        assertThat(result.get(0)).isEqualTo("-4");
    }
}
