package com.advent.day2;

import com.advent.domain.Checksum;

/**
 * Class Description.
 *
 * @author Thomas Plumpton
 */
public class Solution {
    public static void main(String[] args) {
        ChecksumCalculator checksumCalculator = new ChecksumCalculator();

        Checksum checksum = checksumCalculator.calculateChecksum();
        System.out.println("Day 2 - Part 1: " + checksum.getValue());
    }
}
