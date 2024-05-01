import Election.*;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        VotingSystem system = new VotingSystem();

        System.out.print("\nEnter the number of candidates: ");
        // error checking
        int numCandidates = 0;
        while(numCandidates <= 0) {
            while(!input.hasNextInt()) {
                System.out.println("Please enter a positive integer.");
                input.next();
            }
            numCandidates = input.nextInt();
            if(numCandidates <= 0)
                System.out.println("Please enter a positive integer.");
        }
        
        for(int i = 0; i < numCandidates; i++) {
            System.out.print("Enter the name of candidate " + (i+1) + ": ");
            String name = input.next();
            system.addCandidate(name, i+1);
        }
        
        int vote = -1;
        while(true) {
            System.out.print("\n" + system.getFormattedCandidateList() + "\nEnter the ID of the candidate you want to vote for (or enter 0 to stop): ");
            // error checking
            while(!input.hasNextInt()) {
                System.out.println("Please enter a valid ID.");
                input.next();
            }
            vote = input.nextInt();
            if(vote == 0)
                break;
            if(vote < 0 || vote > numCandidates) {
                System.out.println("Please enter a valid ID.");
                continue;
            }
            System.out.println("Vote registered for Candidate " + vote);
            system.addVote(vote);
        }

        system.findWinners();
        System.out.println("\n" + system.getFormattedWinners());
    }
}