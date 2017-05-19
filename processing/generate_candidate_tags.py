import re
import operator

from utils.corenlp import StanfordCoreNLP


CANDIDATE_TAGS = []

def hook_tags(deps):
    words = {}
    for dep in deps:
        if dep['governorGloss'] not in words:
            words[dep['governorGloss']] = dep['governor']
        if dep['dependentGloss'] not in words:
            words[dep['dependentGloss']] = dep['dependent']

    if len(words) > 0:
        sorted_words = sorted(words.items(), key=operator.itemgetter(1))
        tag = ','.join(dict(sorted_words).keys())
        print(tag)
        CANDIDATE_TAGS.append(tag)


def process(deps):
    for i, dep in enumerate(deps):
        if dep['dep'] == 'nsubj':
            if(i<len(deps)-2 and deps[i+1]['dep']=='advmod' and deps[i+2]['dep']=='advmod'):
                hook_tags(deps[i: i+3])
                del deps[i: i+3]
            elif(i<len(deps)-1 and deps[i+1]['dep']=='advmod'):
                hook_tags(deps[i: i+2])
                del deps[i: i+2]
        elif(dep['dep']=='advmod'):
            if(i<len(deps)-1 and (deps[i+1]['dep']=='advmod' or deps[i+1]['dep']=='amod')):
                hook_tags(deps[i: i+2])
                del deps[i: i+2]
            else:
                hook_tags([dep])


if __name__ == '__main__':
    with open('datasets/test_data.txt', 'r') as f:
        comments = map(lambda comment: comment.strip(), f.readlines())

    nlp = StanfordCoreNLP('http://localhost:9000')

    for comment in comments:
        sublines = re.split("，|。|!|\?", comment)
        for subline in sublines:
            if not subline:
                continue

            output = nlp.annotate(subline, properties={
                'annotators': 'tokenize,ssplit,pos,depparse,parse',
                'outputFormat': 'json'
            })
            deps = output['sentences'][0]['basicDependencies']
            process(deps)

    with open('datasets/candidate_tags.txt', 'w') as f:
        for tag in CANDIDATE_TAGS:
            f.write(f"{tag}\n")
