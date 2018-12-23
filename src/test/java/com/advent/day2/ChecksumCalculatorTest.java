package com.advent.day2;

import com.advent.domain.BoxID;
import com.advent.domain.Checksum;
import org.junit.jupiter.api.Tag;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

/**
 * Checksum Calculator
 *
 * @author Thomas Plumpton
 */
class ChecksumCalculatorTest {
    private final ChecksumCalculator checksumCalculator = new ChecksumCalculator();

    @Test
    @Tag("Day2-Part-1")
    void calculateChecksum_exampleInput1() {
        String fileName = "day2/example-input-1-1.txt";
        Checksum result = checksumCalculator.calculateChecksum(fileName);
        assertThat(result.getValue()).isEqualTo(12);
    }

    @Test
    void boxIdContainsDuplicateCharacters_noDuplicates() {
        BoxID id = new BoxID("abcdef");
        boolean result =  checksumCalculator.boxIdContainsDuplicate(id);
        assertThat(result).isFalse();
    }

    @Test
    void boxIdContainsDuplicateCharacters_oneDuplicate() {
        BoxID id = new BoxID("abbcde");
        boolean result =  checksumCalculator.boxIdContainsDuplicate(id);
        assertThat(result).isTrue();
    }

    @Test
    void boxIdContainsDuplicateCharacters_containsDuplicateAndTriplicate() {
        BoxID id = new BoxID("bababc");
        boolean result =  checksumCalculator.boxIdContainsDuplicate(id);
        assertThat(result).isTrue();
    }

    @Test
    void boxIdContainsTriplicateCharacters_containsNoTriplicates() {
        BoxID id = new BoxID("abcdee");
        boolean result =  checksumCalculator.boxIdContainsTriplicate(id);
        assertThat(result).isFalse();
    }

    @Test
    void boxIdContainsTriplicateCharacters_containsDuplicateAndTriplicate() {
        BoxID id = new BoxID("bababc");
        boolean result =  checksumCalculator.boxIdContainsTriplicate(id);
        assertThat(result).isTrue();
    }

    @Test
    void boxIdContainsTriplicateCharacters_containsOneTriplicate() {
        BoxID id = new BoxID("abcccd");
        boolean result =  checksumCalculator.boxIdContainsTriplicate(id);
        assertThat(result).isTrue();
    }

    @Test
    void boxIdsHaveExactlyOneCharacterDifferent_noDifferences() {
        BoxID id = new BoxID("abcdef");
        boolean result = checksumCalculator.boxIdsHaveExactlyOneCharacterDifferent(id, id);
        assertThat(result).isFalse();
    }

    @Test
    void boxIdsHaveExactlyOneCharacterDifferent_oneDifference_lastCharacter() {
        BoxID id = new BoxID("abcdef");
        BoxID id2 = new BoxID("abcdeg");
        boolean result = checksumCalculator.boxIdsHaveExactlyOneCharacterDifferent(id, id2);
        assertThat(result).isTrue();
    }
    @Test
    void boxIdsHaveExactlyOneCharacterDifferent_oneDifference_firstCharacter() {
        BoxID id = new BoxID("abcdef");
        BoxID id2 = new BoxID("bbcdef");
        boolean result = checksumCalculator.boxIdsHaveExactlyOneCharacterDifferent(id, id2);
        assertThat(result).isTrue();
    }

    @Test
    void boxIdsHaveExactlyOneCharacterDifferent_twoDifferences() {
        BoxID id = new BoxID("abcdef");
        BoxID id2 = new BoxID("hbcdeg");
        boolean result = checksumCalculator.boxIdsHaveExactlyOneCharacterDifferent(id, id2);
        assertThat(result).isFalse();
    }

    @Test
    void getBoxIdCommonCharacters_noDifferences() {
        BoxID id = new BoxID("abcdef");
        String result = checksumCalculator.getBoxIdCommonCharacters(id, id);
        assertThat(result).isEqualTo(id.getValue());
    }

    @Test
    void getBoxIdCommonCharacters_oneDifference_firstCharacter() {
        BoxID id = new BoxID("abcdef");
        BoxID id2 = new BoxID("bbcdef");
        String result = checksumCalculator.getBoxIdCommonCharacters(id, id2);
        assertThat(result).isEqualTo("bcdef");
    }

    @Test
    void getBoxIdCommonCharacters_oneDifference_lastCharacter() {
        BoxID id = new BoxID("abcdef");
        BoxID id2 = new BoxID("abcdeg");
        String result = checksumCalculator.getBoxIdCommonCharacters(id, id2);
        assertThat(result).isEqualTo("abcde");
    }

    @Test
    void getBoxIdCommonCharacters_twoDifferences() {
        BoxID id = new BoxID("abcdef");
        BoxID id2 = new BoxID("hbcdeg");
        String result = checksumCalculator.getBoxIdCommonCharacters(id, id2);
        assertThat(result).isEqualTo("bcde");
    }
}
