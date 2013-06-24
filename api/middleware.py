__author__ = 'jared'
class content_response(object):
    def process_response(self, request, response):
        try:
            jreq = request.GET['response_type']
        except:
            jreq = None
        if jreq == 'text_html':
            response['content-type'] = 'text/html'
        return response