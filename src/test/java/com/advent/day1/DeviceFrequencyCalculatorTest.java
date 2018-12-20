package com.advent.day1;

import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

class DeviceFrequencyCalculatorTest {
    private final DeviceFrequencyCalculator deviceFrequencyCalculator = new DeviceFrequencyCalculator();

    @Test
    void calculateResultantFrequency_exampleInput1() {
        String fileName = "example-input-1.txt";
        Frequency resultantFrequency = deviceFrequencyCalculator.calculateResultantFrequency(fileName);
        assertThat(resultantFrequency.getValue()).isEqualTo(3);
    }

    @Test
    void calculateResultantFrequency_exampleInput2() {
        String fileName = "example-input-2.txt";
        Frequency resultantFrequency = deviceFrequencyCalculator.calculateResultantFrequency(fileName);
        assertThat(resultantFrequency.getValue()).isEqualTo(0);
    }

    @Test
    void calculateResultantFrequency_exampleInput3() {
        String fileName = "example-input-3.txt";
        Frequency resultantFrequency = deviceFrequencyCalculator.calculateResultantFrequency(fileName);
        assertThat(resultantFrequency.getValue()).isEqualTo(-6);
    }

    @Test
    void calculateResultantFrequency_dayOneInput() {
        Frequency resultantFrequency = deviceFrequencyCalculator.calculateResultantFrequency();
        assertThat(resultantFrequency.getValue()).isEqualTo(442);
    }
}
