"""Example module."""

from feedly.api_client.session import FeedlySession
from feedly.api_client.stream import StreamOptions
from mcp.server.fastmcp import FastMCP
from feedly_mcp.logging import get_logger


server = FastMCP("Feedly MCP")
logger = get_logger(__name__)


@server.tool()
async def get_ai_news(max_count: int = 10) -> list[dict[str, str]]:
    """Get the latest entries from the AI category.

    Args:
        max_count (int, optional): The maximum number of entries to get. Defaults to 10.

    Returns:
        list[dict[str, str]]: A list of dictionaries of the title and id of the entries.
    """
    session = FeedlySession()
    result = []

    category_name = session.user.user_categories.get("AI")

    for article in category_name.stream_contents(
        options=StreamOptions(max_count=max_count)
    ):
        result.append({"title": article["title"], "id": article["id"]})

    return result


@server.tool()
def mark_as_read(entry_id: str) -> None:
    """Mark an entry as read.

    Args:
        entry_id (str): The id of the entry to mark as read.
    """
    # Log but don't do anything; for testing
    logger.info(f"Marking entry {entry_id} as read.")
    # session = FeedlySession()
    # access_token = session.auth.auth_token
    # url = "https://cloud.feedly.com/v3/markers"

    # headers = {
    #     "Authorization": f"OAuth {access_token}",
    #     "Content-Type": "application/json",
    # }

    # payload = {"action": "markAsRead", "type": "entries", "entryIds": [entry_id]}

    # response = httpx.post(url, json=payload, headers=headers)

    # if response.status_code == 200:
    #     logger.info("Entry marked as read successfully.")
    # else:
    #     logger.error(
    #         f"Failed to mark entry as read. Status code: {response.status_code}"
    #     )
