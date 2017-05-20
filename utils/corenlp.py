import json

import requests


class StanfordCoreNLP(object):
    def __init__(self, server_url):
        if server_url[-1] == '/':
            server_url = server_url[:-1]
        self.server_url = server_url

    def annotate(self, text, properties=None):
        assert isinstance(text, str)
        if properties is None:
            properties = {}
        else:
            assert isinstance(properties, dict)

        try:
            requests.get(self.server_url)
        except requests.exceptions.ConnectionError:
            raise Exception('Check whether you have started the CoreNLP server e.g.\n'
            '$ cd stanford-corenlp-full-2016-10-31/ \n'
            '$ java -Xmx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -serverProperties StanfordCoreNLP-chinese.properties -port 9000 -timeout 15000')

        data = text.encode()
        r = requests.post(
            self.server_url,
            params={
                'properties': str(properties)
            },
            data=data, headers={'Connection': 'close'})
        output = r.text
        if ('outputFormat' in properties and properties['outputFormat'] == 'json'):
            try:
                output = json.loads(output, encoding='utf-8', strict=True)
            except:
                pass
        return output

    def tokensregex(self, text, pattern, filter=False):
        return self.regex('/tokensregex', text, pattern, filter)

    def semgrex(self, text, pattern, filter=False):
        return self.regex('/semgrex', text, pattern, filter)

    def regex(self, endpoint, text, pattern, filter=False):
        r = requests.get(
            self.server_url + endpoint, params={
                'pattern': pattern,
                'filter': filter
            }, data=text)
        output = r.text
        try:
            output = json.loads(r.text)
        except:
            pass
        return output
