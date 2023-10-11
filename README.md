# Optimal-Stopping-Algorithm-Interview-process-using-37 percent-rule

```This project is a deprecated version. A Django based webapp is in the making and will be available here soon with all the features in it.```

This work is inspired  from the book ```Algorithms to live by``` by **Brian Christian and Tom Griffiths** | Trial of 37% rule for the interview process

# Need of this Project :
In Modern Interview Process, It Is Very Important To Record Data Accurately And Efficiently. If You Mess Up Even A Dot, Someone Else Might Pay A Very High Price. On Top Of That It Takes A Lot Of Time To Know Someone And Trust Them In Your Company. But The Most Important And Complex Problem Is Of The Balance Of Time And Quality.


This Mini Project Records Data Of The Candidates In A Systematic Manner And Makes It Easy For The User (Interviewer) To See Visual Output Along With Other Statistics. We Are Taking It One Step Ahead By Implementing Optimal Stopping Algorithm Allowing For The Balance Of Time And Quality Mentioned Above.
On An Average, It Takes About An Hour For A Single Interview To Finish. Even Then, It Seems Very Small In Comparison To “5-6” Hours Interviews Taken By Some Of The Mnc’s. What If There Are 100 Candidates? Will You Give Your 100 Hours For Choosing One Candidate?

The Problem We Are Trying To Solve Is Of Time And Quality. If You Select The Very First Candidate Thinking He/She Seems Good Enough To You, You Might Lose The Opportunity Of Selecting Someone Better In A Little Bit More Time. On The Other Hand, If You Interview Everyone And Consider The Top Rankers For Selection, You’ve Already Lost All Of Your Precious Time.IfYouAreHiringForAWellEstablished Company,You Might Not Bother About Time And Look For Only The Best.

Now The Problem Comes For The **Small Companies**, Say A Start-Up. If You Are Hiring For A Start-Up, And the Project's And Deadline Is Just Next Month. After doing The Math And It Occurs To You That There Is A Chance That You Might Not Meet The Deadline With current Number Of Employees. So You Decide To Hire Some Freshmen To Share The Burden. You Contact Nearby College Looking For Good Enough Candidates For Your Task.
The Problem With The Word ***“Good Enough”*** Is It’s Definition. In Certain Situations A Barely Passed Candidate Might Be “Good Enough”, And Sometimes Even 80 Percentile Seems A Bit Low For The “Good Enough”. Fortunately, After You Are done With calculating your own threshold, It Depends On The **Overall Average** Of The Pool You Are Searching In. Again Here, I Said “Overall”, Which Means Complete Average Of The Pool, For Which You’ll Have To Take Everyone’s Interview, Which Seems Impractical When You Can Select The Best And Not Only The Average After Everyone’s Interview.

The Solution To This Problem Is Same As Many Other Problems Like The Secretary Problem, The Stable Marriage Problem, House Searching, Toilet Hunting,Etc. And It Is Called ***Optimal Stopping problem***. It Utilises The Runtime Pool Average And ***Balances The Time And The Quality***.

# Dependencies :
 Libraries
 ```time```,
 ```CSV```,
 ```math```
 these libraries will come by default with correct python version.
 
 If you find import error use pip.
 
 ```pip install time```
 
 
 for **Sci-Kit Learn**  
 ```import sklearn```
 
 Assumptions (What I expect to already be installed):

Python 3.6 installed
Pip installed (If it is not already installed, download and install pip: 

https://pip.pypa.io/en/stable/installing/)

Install numpy: ```pip install numpy```


Install scipy: ```pip install scipy```


Install sklearn: ```pip install sklearn```

Test installation by opening a python interpreter and importing sklearn:
python
```import sklearn```

If it successfully imports (no errors), then sklearn is installed correctly.

[Sci-kit learn Documentation](scikit-learn.org/stable/documentation.html)


# Decision Tree Classifier :

[Decision Tree Classifier Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)

[This medium Article](https://medium.com/machine-learning-101/chapter-3-decision-trees-theory-e7398adac567) helped me understand the theory :

 

# There are two phases namely :

**Lookup Phase :**
In this phase 37% of the candidates will be interviewed and their data will be collected. Interviewer will have full command over selection or rejection. Features and lebels will be collected based on interviewer's Decision. This phase will end when 37% of the candidates have been interviewed. This phase might end without the start of next phase if the interviewer encounteres  Required number of "Good Enough" candidates (in terms of overall Quality) in the lookup phase based on their requirements. 

**Selection Phase :** 
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
[Ankit](https://github.com/ankit2web), 
[Husain](https://github.com/husainshaikh895)


# Copyright
[Husain Akbar Shaikh](https://www.github.com/HusainShaikh895) ( husainshaikhwork@gmail.com )
