/**
 * Autocompleter.java
 * Jeff Ondich, 20 March 2018
 *
 * This class exposes a very simple interface for generating auto-completions of search strings.
 * The purpose of this class is to give the students in CS257 an opportunity to practice creating
 * unit tests.
 */
package edu.carleton.jondich;

import java.util.ArrayList;
import java.util.List;

public class Autocompleter {
    public Autocompleter() {
        // Initialization goes here, as needed. For example, you might load
        // from a file into a list (or a hashmap or something like that)
        // the list of strings that are going to form the dataset of potential
        // auto-completions. The initialization will be up to you.
    }

    /**
     * @param searchString the string whose autocompletions are sought
     * @return the list of potential completions that match the search string,
     *  sorted in decreasing order of quality of the match (that is, the matches
     *  are sorted from best match to weakest match)
     */
    public List<String> getCompletions(String searchString) {
        return new ArrayList<String>();
    }
}