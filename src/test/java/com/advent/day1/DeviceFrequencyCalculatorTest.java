package com.advent.day1;

import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

class DeviceFrequencyCalculatorTest {
    private final DeviceFrequencyCalculator deviceFrequencyCalculator = new DeviceFrequencyCalculator();

    @Test
    void calculateResultantFrequency_exampleInput1() {
        String fileName = "example-input-1.txt";
        Integer resultantFrequency = deviceFrequencyCalculator.calculateResultantFrequency(fileName);
        assertThat(resultantFrequency).isEqualTo(3);
    }

    @Test
    void calculateResultantFrequency_exampleInput2() {
        String fileName = "example-input-2.txt";
        Integer resultantFrequency = deviceFrequencyCalculator.calculateResultantFrequency(fileName);
        assertThat(resultantFrequency).isEqualTo(0);
    }

    @Test
    void calculateResultantFrequency_exampleInput3() {
        String fileName = "example-input-3.txt";
        Integer resultantFrequency = deviceFrequencyCalculator.calculateResultantFrequency(fileName);
        assertThat(resultantFrequency).isEqualTo(-6);
    }
}
