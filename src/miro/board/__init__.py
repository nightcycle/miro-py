import requests
from typing import TypedDict, Literal, Any

SortType = Literal["default", "last_modified", "last_opened", "last_created", "alphabetically"]

class Board():
	id: str
	def __init__(self):
		self.id = ""

def get_all(
	team_id: str | None = None,
	project_id: str | None = None, 
	owner: str | None = None, 
	limit=20, 
	offset=0, 
	sort: SortType="default"
) -> list[Board]:
	return []
