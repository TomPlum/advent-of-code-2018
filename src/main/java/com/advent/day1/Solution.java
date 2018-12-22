package com.advent.day1;

public class Solution {
    public static void main(String[] args) {
        DeviceFrequencyCalculator calculator = new DeviceFrequencyCalculator();
        Frequency resultantFrequency = calculator.getResultantFrequency();
        System.out.println(resultantFrequency.getValue());
    }
}
