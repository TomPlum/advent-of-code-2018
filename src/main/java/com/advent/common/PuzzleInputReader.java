package com.advent.common;

import com.advent.domain.Frequency;

import java.io.IOException;
import java.net.URISyntaxException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;

public class PuzzleInputReader {
    public static List<Frequency> readPuzzleInput(Integer dayNumber) {
        return readInputAsFrequency(createFileName(dayNumber));
    }

    private static String createFileName(Integer dayNumber) {
        return "day-" + dayNumber + "-input.txt";
    }

    private static Path getPath(String fileName) {
        try {
           return Paths.get(PuzzleInputReader.class.getClassLoader().getResource(fileName).toURI());
        } catch (URISyntaxException | NullPointerException e) {
            throw new RuntimeException("Cannot Find Resource " + fileName);
        }
    }

    public static List<Integer> readInputAsInteger(String fileName) {
        return readFile(fileName).stream().map(Integer::parseInt).collect(Collectors.toList());
    }

    public static List<Frequency> readInputAsFrequency(String fileName) {
        return readFile(fileName).stream().map(v -> new Frequency(Integer.parseInt(v))).collect(Collectors.toList());
    }

    public static List<String> readFile(String fileName) {
        try {
            return Files.readAllLines(getPath(fileName));
        } catch (IOException e) {
            throw new RuntimeException("Cannot Read File @ " + fileName);
        }
    }
}
