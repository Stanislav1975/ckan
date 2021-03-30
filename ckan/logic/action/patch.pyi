from typing import Dict
from ckan.types import Context, DataDict

def package_patch(context: Context, data_dict: DataDict) -> Dict: ...
def resource_patch(context: Context, data_dict: DataDict) -> Dict: ...
def group_patch(context: Context, data_dict: DataDict) -> Dict: ...
def organization_patch(context: Context, data_dict: DataDict) -> Dict: ...
def user_patch(context: Context, data_dict: DataDict) -> Dict: ...