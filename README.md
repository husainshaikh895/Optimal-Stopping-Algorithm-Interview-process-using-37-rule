# Optimal-Stopping-Algorithm-Interview-process-using-37-rule
This work is inspired  from the book ```Algorithms to live by``` by **Brian Christian and Tom Griffiths** | Trial of 37% rule for the interview process

So, the problem is of Balancing of Time and Quality.
You are an interviewer, you have a deadline to select 5 candidates among 200. You can't interview all of them and sort according to their scores, because you have a deadline. You can't select the first five candidates because you haven't seen what others are like.
We approach this problem with Optimal Stopping Algorithm which is pretty famous in the Software Industry. Specifically we will use 37% rule. We are using Decision Tree Classifier to classify the candidates ( Selected or Rejected ). We will pass the features and label to later predictions into the fit().


# There are two phases namely :

# Lookup Phase : 
In this phase 37% of the candidates will be interviewed and their data will be collected. Interviewer will have full command over selection or rejection. Features and lebels will be collected based on interviewer's Decision. This phase will end when 37% of the candidates have been interviewed. This phase might end without the start of next phase if the interviewer encounteres  Required number of "Good Enough" candidates (in terms of overall Quality) in the lookup phase based on their requirements. 

# Selection Phase : 
In this Phase the candidates will be considered for selection by the algorithm based on previous data. Decision tree classifier will suggest whether this candidate should be selected or not. This phase will end if the total candidates are over or required candidates have been selected.


# Features:
- First 37% of the candidates will be judged and data will be collected.
- Later Candidates will be considered for selection
- Interviewer will have the full command to select or reject the candidate in LookupPhase
- Machine Learning will assist the Algorithm 
- Data will be saved systematically and locally in a CSV file
- Statistics will be shown after the process is done
- Graphs will be plotted using matplotlib

# Future ideas :
- Put the lookup Phase candidates in "Maybe" and consider them later if you don't get required number of candidates when 70% of the candidates have been interviewed
- Use gmail API to send them(selected candidates) offer letter directly after the process is done
- Implement a Graphical User Interface
- Put security restrictions (Authentication)
- Put CSV of all the eligible candidates before the process so it will authenticate candidates directly and collect prerequisites of theirs, eg. PRN, Name, Scores in Aptitude, etc.

# Contributors:
None as of Now.


# Copyright
[Husain Akbar Shaikh](https://www.github.com/HusainShaikh895) ( shaikhhusain895@gmail.com )
