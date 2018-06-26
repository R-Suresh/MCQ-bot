# MCQ Bot

This is the dataset of networking based books
The file source4 is the one that we want to modify
Remove all unnecessary stuff from it .
Make the entire file as a single paragraph.

Also make sure the modified file at each stage is in ansi encoding

Added notes about possible architecture to model_architecture.txt

Furthermore the question bank is added, the number of questions in each file indicated by the title of the file
## Overall model architecture
![qa-lstm-attn](https://user-images.githubusercontent.com/36242729/41887663-549e80f0-791f-11e8-889c-3237ceab283e.png)

## Updates

Create an updates folder and post daily updates on it. All of us put in lines about daily contributions
Add neccecary txt files

## Research papers 

Links to all papers refered in the project

## Requirements

### Software 
 ```
 1. Tensorflow - 1.8 or higher
 2. Keras - 2.0.6 
 3. Jupyter notebook
 4. matplotlib
 5. seaborn
 6. nltk
 7. gensim
 ``` 
### Hardware

 If using ```tensorflow-gpu``` a graphics card is needed
## Word embeddings

To be added by rahul

## Text Pre-Processing

 To be added by shubham
 <img src="docs/pre-processing.jpeg"/>

## Running the model

Go to the exam-bot-ccna directory, then run the following files:

1. flashcard-embedding.ipynb
2. qa-blstm-fem-attn.ipynb

## Current Model


### QA-LSTM with Attention

Problem with RNNs in general is the vanishing gradient problem. While LSTMs address the problem, they still suffer from it because of the very long distances involved in QA contexts. The solution to this is attention, where the network is forced to look at certain parts of the context and ignore (in a relative sense) everything else.

<img src="docs/qa-lstm-attn.png"/>

### Incorporating External Knowledge

Based on the competition message boards, there seems to be general consensus that external content is okay to use. Here are some mentioned:

* [ConceptNet](http://conceptnet5.media.mit.edu/)
* [CK-12 books](http://www.ck12.org/student/)
* [Quizlets](https://quizlet.com/)
* [Studystack Flashcards](http://www.studystack.com/)

Most of the contents mentioned involve quite a lot of effort to scrape/crawl the sites and parse the crawled content. There was one content source (Flashcards from StudyStack) that was [available here](https://drive.google.com/file/d/0B0fFJSGDUPcgUFJpTVl3QXhnNTQ/view?usp=sharing) in pre-parsed form, so I used that. This gave me 400k flashcard records, questions followed by the correct answer. I thought of this as the "story" from the bAbI context.

<img src="docs/flashcard-format.png"/>

### QA-LSTM with Attention and Custom Embedding

My first attempt at incorporating the story was to replace the embedding from the pre-trained Word2Vec model with a Word2Vec model generated using the Flashcard data. This created a smaller, more compact embedding and gave me quite a good boost in accuracy.

| Model                              | Default Embedding | Story Embedding |
| -----------------------------------| ----------------- | --------------- |
| QA-LSTM w/Attention                | 62.93%            | 76.27%          |
| QA-LSTM bidirectional w/Attention  | 60.43%            | 76.27%          |

The qa-lstm-fem-attn model(s) are identical to the qa-lstm-attn model(s) except for the embedding used - instead of the default embedding from Word2Vec, I am now using a custom embedding from the flashcard data.

