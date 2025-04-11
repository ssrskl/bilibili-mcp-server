from loguru import logger
import requests

def make_request(url, method='GET', **kwargs):
    """
    发送网络请求并处理异常。
    
    参数:
        url (str): 请求的目标 URL
        method (str): HTTP 方法，默认为 'GET'
        **kwargs: 其他参数，如 headers、data、params、timeout 等
    
    返回:
        requests.Response: 成功时的响应对象
    
    抛出:
        NetworkError: 网络请求失败时的自定义异常
    """
    logger.info(f"发送 {method} 请求到 {url}")
    try:
        response = requests.request(method, url, **kwargs)
        response.raise_for_status()  # 检查 HTTP 状态码，异常时抛出
        logger.info(f"接收到状态码为 {response.status_code} 的响应")
        return response
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP 错误: {e.response.status_code} - {e.response.text}")
        raise NetworkError(f"HTTP 错误: {e.response.status_code} - {e.response.text}")
    except requests.exceptions.ConnectionError as e:
        logger.error("连接错误: 无法连接到服务器")
        raise NetworkError("连接错误: 无法连接到服务器")
    except requests.exceptions.Timeout as e:
        logger.error("超时错误: 请求超时")
        raise NetworkError("超时错误: 请求超时")
    except requests.exceptions.RequestException as e:
        logger.error(f"发生错误: {e}")
        raise NetworkError(f"发生错误: {e}")