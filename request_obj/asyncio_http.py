import requests
import asyncio
import user_agent
from request_obj.enums import Methods, Formats

class Request(object):

    __available_methods = ("POST", "GET", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS")
    __available_formats = ("JSON",)

    def __init__(self, name: str, method: Methods, url: str, payload: dict, headers: dict):
        self.__name = name
        self.__method = method
        self.__url = url
        self.__payload = payload
        self.__headers = headers
        self.__response = None
        self.__response_format = None
        self.__response_status_code = None

    @staticmethod
    def init(function_name):
        asyncio.run(function_name())

    @staticmethod
    async def available_methods() -> tuple:
        """Shows all available HTTP methods"""
        return Request.__available_methods

    @staticmethod
    async def available_formats() -> tuple:
        """Shows all available request response formats"""
        return Request.__available_formats

    @staticmethod
    async def generate_user_agent(os=None, navigator=None, platform=None, device_type=None):
        """Generates User-Agent for HTTP-request header"""
        user_agent.generate_user_agent(os, navigator, platform, device_type)

    async def get_method(self) -> Methods:
        """Get request method"""
        return self.__method

    async def get_url(self) -> str:
        """Get request URL"""
        return self.__url

    async def get_payload(self) -> dict:
        """Get request payload"""
        return self.__payload

    async def get_headers(self) -> dict:
        """Get request headers"""
        return self.__headers

    async def get_name(self) -> str:
        """Get request name"""
        return self.__name

    async def get_last_response(self) -> tuple:
        """Get last request response (returns: response_status_code, response, response_format)"""
        return self.__response, self.__response_format

    async def send(self, format: Formats = Formats.JSON, register_response_as_last: bool = True):
        """Send HTTP-request"""
        if format == Formats.JSON:
            req = self.__method(self.__url, headers=self.__headers, data=self.__payload).json()
        elif format == Formats.DEFAULT:
            req = self.__method(self.__url, headers=self.__headers, data=self.__payload)
        if register_response_as_last:
            self.__response = req
            self.__response_format = format
            self.__response_status_code = req.status_code
