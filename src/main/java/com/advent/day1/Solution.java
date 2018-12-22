package com.advent.day1;

import com.advent.domain.Frequency;

public class Solution {
    public static void main(String[] args) {
        DeviceFrequencyCalculator calculator = new DeviceFrequencyCalculator();

        Frequency resultantFrequency = calculator.getResultantFrequency();
        System.out.println("Day 1 - Part 1: " + resultantFrequency.getValue());

        Frequency firstDuplicateFrequency = calculator.getFirstDuplicateFrequency();
        System.out.println("Day 1 - Part 2: " + firstDuplicateFrequency.getValue());
    }
}
