package com.advent.common;

import com.advent.domain.Frequency;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;

class PuzzleInputReaderTest {
    @Test
    void readTestInput() {
        String fileName = "test-input.txt";
        List<String> result = PuzzleInputReader.readFile(fileName);
        assertThat(result.get(0)).isEqualTo("Hello World!");
    }

    @Test
    void readPuzzleInput() {
        Integer dayNumber = 1;
        List<Frequency> result = PuzzleInputReader.readPuzzleInput(dayNumber);
        assertThat(result.get(0).getValue()).isEqualTo(-4);
    }
}
