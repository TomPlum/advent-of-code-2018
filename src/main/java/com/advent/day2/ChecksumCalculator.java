package com.advent.day2;

import com.advent.common.PuzzleInputReader;
import com.advent.domain.BoxID;
import com.advent.domain.Checksum;

import java.util.List;

/**
 * Checksum Calculator
 *
 * @author Thomas Plumpton
 */
public class ChecksumCalculator {
    public Checksum calculateChecksum(String fileName) {
        List<String> puzzleInput = PuzzleInputReader.readFile(fileName);
        return formulateChecksum(puzzleInput);
    }

    public Checksum calculateChecksum() {
        return formulateChecksum(PuzzleInputReader.readPuzzleInputAsString(2));
    }

    protected Checksum formulateChecksum(List<String> puzzleInput) {
        Integer duplicates = getDuplicates(puzzleInput);
        Integer triplicates = getTriplicates(puzzleInput);
        return new Checksum(duplicates * triplicates);
    }

    protected Integer getDuplicates(List<String> puzzleInput) {
        int duplicates = 0;
        for (String boxId : puzzleInput) {
            if (boxIdContainsDuplicate(new BoxID(boxId))) {
                duplicates++;
            }
        }
        return duplicates;
    }

    protected Integer getTriplicates(List<String> puzzleInput) {
        int triplicates = 0;
        for (String boxId : puzzleInput) {
            if (boxIdContainsTriplicate(new BoxID(boxId))) {
                triplicates++;
            }
        }
        return triplicates;
    }

    protected boolean boxIdContainsDuplicate(BoxID id) {
       return boxIdContainsRecurringCharacter(id, 2);
    }

    public boolean boxIdContainsTriplicate(BoxID id) {
        return boxIdContainsRecurringCharacter(id, 3);
    }

    private boolean boxIdContainsRecurringCharacter(BoxID id, int recurringTimes) {
        int count = 0;
        char[] characters = id.getValue().toCharArray();
        for (char searchChar : characters) {
            for (char idChar : characters) {
                if (idChar == searchChar) {
                    count++;
                }
            }
            if (count == recurringTimes) {
                return true;
            }
            count = 0;
        }
        return false;
    }

    public boolean boxIdsHaveExactlyOneCharacterDifferent(BoxID id, BoxID id2) {
        int differingCharacters = 0;
        char[] firstIdCharacters = id.getValue().toCharArray();
        char[] secondIdCharacters = id2.getValue().toCharArray();

        for (int i = 0; i < id.getValue().length(); i++) {
            if (firstIdCharacters[i] != secondIdCharacters[i]) {
                differingCharacters++;
            }
        }

        return differingCharacters == 1;
    }

    public String getBoxIdCommonCharacters(BoxID id, BoxID id2) {
        StringBuffer commonCharacters = new StringBuffer();
        char[] firstIdCharacters = id.getValue().toCharArray();
        char[] secondIdCharacters = id2.getValue().toCharArray();

        for (int i = 0; i < id.getValue().length(); i++) {
            if (firstIdCharacters[i] == secondIdCharacters[i]) {
                commonCharacters.append(firstIdCharacters[i]);
            }
        }

        return commonCharacters.toString();
    }
}
