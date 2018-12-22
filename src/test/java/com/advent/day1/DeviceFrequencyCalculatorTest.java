package com.advent.day1;

import org.junit.jupiter.api.Tag;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

class DeviceFrequencyCalculatorTest {
    private final DeviceFrequencyCalculator deviceFrequencyCalculator = new DeviceFrequencyCalculator();

    @Test
    @Tag("Day 1 - Part 1")
    void calculateResultantFrequency_exampleInput1() {
        String fileName = "day1/example-input-1-1.txt";
        Frequency resultantFrequency = deviceFrequencyCalculator.getResultantFrequency(fileName);
        assertThat(resultantFrequency.getValue()).isEqualTo(3);
    }

    @Test
    @Tag("Day 1 - Part 1")
    void calculateResultantFrequency_exampleInput2() {
        String fileName = "day1/example-input-1-2.txt";
        Frequency resultantFrequency = deviceFrequencyCalculator.getResultantFrequency(fileName);
        assertThat(resultantFrequency.getValue()).isEqualTo(0);
    }

    @Test
    @Tag("Day 1 - Part 1")
    void calculateResultantFrequency_exampleInput3() {
        String fileName = "day1/example-input-1-3.txt";
        Frequency resultantFrequency = deviceFrequencyCalculator.getResultantFrequency(fileName);
        assertThat(resultantFrequency.getValue()).isEqualTo(-6);
    }

    @Test
    @Tag("Day 1 - Part 1")
    void calculateResultantFrequency_dayOneInput() {
        Frequency resultantFrequency = deviceFrequencyCalculator.getResultantFrequency();
        assertThat(resultantFrequency.getValue()).isEqualTo(442);
    }

    @Test
    @Tag("Day 1 - Part 2")
    void calculateFirstDuplicateResultantFrequency_exampleInput1() {
        String fileName = "day1/example-input-2-1.txt";
        Frequency duplicateFrequency = deviceFrequencyCalculator.calculateFirstDuplicateFrequency(fileName);
        assertThat(duplicateFrequency).isEqualTo(0);
    }

}
