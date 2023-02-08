import requests
from requests.adapters import HTTPAdapter
#from requests.packages.urllib3.util.retry import Retry     ■ Import "requests.packages.urllib3.util.retry" could not be resolved
from urllib3.util import Retry
from requests.adapters import HTTPAdapter
from ratelimit import limits, RateLimitException, sleep_and_retry

DEFAULT_TIMEOUT = 5 # seconds
ONE_MINUTE = 60
MAX_CALLS_PER_MINUTE = 120

@sleep_and_retry
@limits(calls=MAX_CALLS_PER_MINUTE, period=ONE_MINUTE)
class TimeoutHTTPAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        self.timeout = DEFAULT_TIMEOUT
        if "timeout" in kwargs:
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        timeout = kwargs.get("timeout")
        if timeout is None:
            kwargs["timeout"] = self.timeout
        return super().send(request, **kwargs)

class NewSession(object):
    headers = {
        "Content-Type": "application/json", "Accept": "application/json", }


    retry_strategy = Retry(total=10,
                       backoff_factor=1,
                       status_forcelist=[500, 502, 503, 504],
                       method_whitelist=['GET', 'POST'])
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session = requests.Session()
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    @sleep_and_retry
    @limits(calls=MAX_CALLS_PER_MINUTE, period=ONE_MINUTE)
    def get(self, url: str, endpoint: str, params: dict=dict()):
        """Performs HTTP Get Requests"""
        url = f"{url}{endpoint}"
        try:
            response = None
            if params:
                response = self.session.get(url=url, headers=self.headers, params=params)
            else:
                response = self.session.get(url=url, headers=self.headers)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as err:
            print(err)
            return requests.Response

    @sleep_and_retry
    @limits(calls=MAX_CALLS_PER_MINUTE, period=ONE_MINUTE)
    def post(self, url: str, endpoint: str):
        """Peforms HTTP Post Requests"""
        url = f"{url}{endpoint}"
        try:
            response = self.session.post(url=url, headers=self.headers)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as err:
            print(err)
            return requests.Response

    def query(self, url: str, endpoint: str, params: dict):
        '''Performs a HTTP query request'''
        return  self.get(url, endpoint, params)
