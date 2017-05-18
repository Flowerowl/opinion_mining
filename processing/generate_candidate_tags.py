import re
import operator

from utils.corenlp import StanfordCoreNLP


def sort_by_position(words):
    sorted_words = sorted(words.items(), key=operator.itemgetter(1))
    words = ''.join(dict(sorted_words).keys())

    return

def extract_candidate_tags(deps):
    candidate_tags = []

    for i, dep in enumerate(deps):
        if dep['dep'] == 'nsubj':
            if(i<len(deps)-2 and deps[i+1]['dep']=='advmod' and deps[i+2]['dep']=='advmod'):
                words = {}
                for j in range(3):
                    temp = deps[i+j]
                    if temp['governorGloss'] not in words:
                        words[temp['governorGloss']] = temp['governor']
                    if temp['dependentGloss'] not in words:
                        words[temp['dependentGloss']] = temp['dependent']
                if len(words) > 0:
                    sentence = sort_by_position(words)
                    candidate_tags.append(sentence)
            elif(i<len(deps)-1 and deps[i+1]['dep']=='advmod'):
                words = {}
                for j in range(2):
                    temp = deps[i+j]
                    if temp['governorGloss'] not in words:
                        words[temp['governorGloss']] = temp['governor']
                    if temp['dependentGloss'] not in words:
                        words[temp['dependentGloss']] = temp['dependent']
                if len(words) > 0:
                    sentence = sort_by_position(words)
                    candidate_tags.append(sentence)
        elif(dep['dep']=='advmod'):
            if(i<len(deps)-1 and deps[i+1]['dep']=='advmod'):
                words = {}
                for j in range(2):
                    temp = deps[i+j]
                    if temp['governorGloss'] not in words:
                        words[temp['governorGloss']] = temp['governor']
                    if temp['dependentGloss'] not in words:
                        words[temp['dependentGloss']] = temp['dependent']
                if len(words) > 0:
                    sentence = sort_by_position(words)
                    candidate_tags.append(sentence)
            elif(i<len(deps)-1 and deps[i+1]['dep']=='amod'):
                words = {}
                for j in range(2):
                    temp = deps[i+j]
                    if temp['governorGloss'] not in words:
                        words[temp['governorGloss']] = temp['governor']
                    if temp['dependentGloss'] not in words:
                        words[temp['dependentGloss']] = temp['dependent']
                if len(words) > 0:
                    sentence = sort_by_position(words)
                    candidate_tags.append(sentence)
            else:
                words = {}
                temp = dep
                words[temp['governorGloss']] = temp['governor']
                words[temp['dependentGloss']] = temp['dependent']
                if len(words) > 0:
                    sentence = sort_by_position(words)
                    candidate_tags.append(sentence)

    import pdb; pdb.set_trace()

    return candidate_tags


if __name__ == '__main__':
    with open('datasets/test_data.txt', 'r') as f:
        comments = map(lambda comment: comment.strip(), f.readlines())

    nlp = StanfordCoreNLP('http://localhost:9000')

    sublines = re.split(";|,|\*|\n|\.|，|。|!|\?", list(comments)[0])
    output = nlp.annotate(sublines[0], properties={
        'annotators': 'tokenize,ssplit,pos,depparse,parse',
        'outputFormat': 'json'
    })
    deps = output['sentences'][0]['basicDependencies']

    candidate_tags = extract_candidate_tags(deps)
