package com.advent.common;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.Objects;

public class PuzzleInputReader {
    public static List<String> readPuzzleInput(Integer dayNumber) {
        String fileName = createFileName(dayNumber);
        Path filePath = getPath(fileName);
        return readFile(filePath);
    }

    private static String createFileName(Integer dayNumber) {
        return "day-" + dayNumber + "-input.txt";
    }

    private static Path getPath(String fileName) {
        Path filePath = null;
        try {
            URI uri = PuzzleInputReader.class.getClassLoader().getResource(fileName).toURI();
            filePath = Paths.get(uri);
        } catch (URISyntaxException e) {
            e.printStackTrace();
        }
        return filePath;
    }

    public static List<String> readInput(String fileName) {
        return readFile(getPath(fileName));
    }

    private static List<String> readFile(Path filePath) {
        try {
            return Files.readAllLines(filePath);
        } catch (IOException e) {
            throw new RuntimeException("Cannot Read File @ " + filePath.toString());
        }
    }
}
