package Election;

import java.util.*;

public class VotingSystem {
    private ArrayList<Candidate> candidateList = new ArrayList<Candidate>();
    private HashMap<Candidate, Integer> candidateVotes = new HashMap<Candidate, Integer>();
    private ArrayList<Candidate> winners = new ArrayList<Candidate>();

    // constructors
    public VotingSystem(ArrayList<Candidate> cl, HashMap<Candidate, Integer> cv) {
        candidateList = cl;
        candidateVotes = cv;
        winners.clear();
    }

    public VotingSystem(ArrayList<Candidate> cl) {
        candidateList = cl;
        candidateVotes.clear();
        winners.clear();
    }

    public VotingSystem() {
        candidateList.clear();
        candidateVotes.clear();
        winners.clear();
    }

    // setters
    public void setCandidateList(ArrayList<Candidate> cl) {
        candidateList = cl;
    }

    public void setCandidateVotes(HashMap<Candidate, Integer> cv) {
        candidateVotes = cv;
    }

    public void setWinners(ArrayList<Candidate> w) {
        winners = w;
    }

    // getters
    public ArrayList<Candidate> getCandidateList() {
        return candidateList;
    }

    public HashMap<Candidate, Integer> getCandidateVotes() {
        return candidateVotes;
    }

    public ArrayList<Candidate> getWinners() {
        return winners;
    }

    public int getNumberOfCandidates() {
        return candidateList.size();
    }
    
    public void addCandidate(String name, int id) {
        Candidate c = new Candidate(name, id);
        candidateList.add(c);
        candidateVotes.put(c, 0);
    }

    public void addCandidate(Candidate c) {
        candidateList.add(c);
        candidateVotes.put(c, 0);
    }

    public String getFormattedCandidateList() {
        String output = "Candidates:\n";
        for(int i = 0; i < candidateList.size(); i++)
            output += candidateList.get(i).toString();
        
        return output;
    }

    public String getFormattedWinners() {
        String output = "Winners:\n";
        for(int i = 0; i < winners.size(); i++)
            output += winners.get(i).toStringWinner();
        
        return output;
    }

    public void addVote(int i) {
        candidateList.get(i-1).addVote();
    }

    private void updateVotes() {
        for(Map.Entry<Candidate, Integer> entry : candidateVotes.entrySet())
            candidateVotes.replace(entry.getKey(), entry.getKey().getVotes());
    }

    private int getMaxVotes() {
        updateVotes();
        int maxVotes = 0;
        for(Map.Entry<Candidate, Integer> entry : candidateVotes.entrySet())
            if(entry.getValue() > maxVotes)
                maxVotes = entry.getValue();
        return maxVotes;
    }

    public void findWinners() {
        int maxVotes = getMaxVotes();
        for(Candidate c : candidateVotes.keySet()) {
            int votes = candidateVotes.get(c);
            if(votes == maxVotes)
                winners.add(c);
        }
    }
}