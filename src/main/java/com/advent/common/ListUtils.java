package com.advent.common;

import java.util.List;

/**
 * List Utility
 *
 * @author Thomas Plumpton
 */
public class ListUtils {
    public static <E> E getLastElement(List<E> list) {
        return list.get(list.size() - 1);
    }
}
