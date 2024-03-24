Gives a psychological analysis of a desired Twitter user. 
Dependencies needed are HuggingFace's Transformers library, PyTorch, and Tweety. To run the program just add the required dependencies and run main.py with the other provided py files in the same folder.

ROADMAP:
1. Further fine tuning the AI model with more psychological information. 
   Examples:
   DSM 5, Big 5, Enneagram data, Myers Briggs, therapist/psychiatrist notes, premade psychology datasets (specifically for AI models), DISC assessment criteria, psycholinguistics, criminal profiling data, books/talks from current top psychoanalysts, Jungian archetypes and theory, APA database, lectures, studies, etc

2. Increase memory effectiveness and efficiency of the AI model in order to shorten the very long analysis time.

3. Allow the user to choose how many pages of tweets they would like to put in the model (currently set to 1 due to model constraints and already high memory and time requirements).

4. Find a scraping method not under Twitter's limitations to allow for unlimited scraping without needing to provide a username and password.

5. (MAYBE) Cut number of parameters down to those necessary for coherence and psychological understanding or start fresh with a new custom model and datasets.

6. (MAYBE) Change the way links and retweets are input to eliminate extra unnecessary characters in the prompt to speed up the model (due to links being unnecessary and retweets not reflecting psychologically the same as normal tweets which are in the user's own words).

7. (MAYBE) Setup more AI functions/models to get better analysis. Ex. Could have one summary model which gives a summary of ideas then feeds that to the psychological model where the analysis model can be purely focused on psychology ideas rather than having to do both.
   Another good example could be adding a model which rather than text generation generates a number for certain criteria (ex Myers Briggs variables) which is put into the prompt for the final psychological analysis.
   The problem with this is increasing memory and time requirements but that could be negated by using more lightweight custom models for different functions.

8. Allowing the user to get psychological analysis of more than just specific users. Aggregate psychological analysis could be done on certain keywords, hashtags, etc which would use a different function focused on psychologically analyzing groups of people.
   
9. Adding more available platforms like reddit.

10. (MAYBE) Add an image recognition model which can summarize images allowing for more data, increased functionality, and the ability to use the program concept on even image platforms like instagram and snapchat.
