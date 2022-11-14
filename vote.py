"\n"
"\n"

party_1 = input("Enter the party of the first candidate : ")
party_2 = input("Enter the party of the second candidate : ")

nominee_1 = input("Enter the name of Candidate 1: ")
nominee_2 = input("Enter the name of Candidate 2 ")

print("The candidate of", party_1, "is", nominee_1)

print("The candidate of", party_2, "is", nominee_2)


nom_1_votes = 0
nom_2_votes = 0

votes_id = [1,2,3]

num_of_voter = len(votes_id)

while True:
    if votes_id == []:
        print("-------------Voting Session Over! ------------------")
        if nom_1_votes > nom_2_votes:
            percent = (nom_1_votes/num_of_voter)*100
            print("------------", nominee_1, "has Won", "with", percent, "%  votes!-------------")
            break

        elif nom_2_votes > nom_1_votes:
            percent = (nom_2_votes/num_of_voter)*100
            print("--------------", nominee_2, "has Won", "with", percent, "%  votes!----------")
            break    

    else:
        voter = int(input("Enter your voter ID no : "))
        if voter in votes_id:
            print("You are eligble to vote ")
            votes_id.remove(voter)
            print("*********** VOTING INSTRUCTION: ENTER 1 FOR", nominee_1, "AND 2 FOR", nominee_2,"********")
            vote = int(input("Enter your vote 1 or 2 : "))
            
            if vote == 1:
                nom_1_votes+=1
                print("^^^^ Thank you for casting your vote! ^^^^")

            elif vote == 2:
                nom_2_votes+=1
                print("^^^^ Thank you for casting your vote! ^^^^")
        else:
            print("**** You are not eligble to vote or you have already voter! ***")        
        