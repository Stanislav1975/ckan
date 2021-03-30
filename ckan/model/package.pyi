
from ckan.types import Query
from ckan.model.package_relationship import PackageRelationship
from ckan.model.tag import PackageTag
import datetime
from typing import (
    Dict,
    List,
    Optional,
    TYPE_CHECKING,
    Tuple,
    Union,
    Any,
)
import ckan.lib.maintain as maintain
from sqlalchemy import Table
from ckan.model import core, domain_object

if TYPE_CHECKING:
    from .activity import Activity
    from .user import User
    from .resource import Resource
    from .tag import PackageTag
    from .group import Group
    from .vocabulary import Vocabulary
    from .license import LicenseRegister, License

PACKAGE_NAME_MAX_LENGTH: int = 100
PACKAGE_NAME_MIN_LENGTH: int = 2
PACKAGE_VERSION_MAX_LENGTH: int = 100
package_table: Table

class Package(core.StatefulObjectMixin, domain_object.DomainObject):
    id: str
    name: str
    title: str
    version: str
    url: str
    author: str
    author_email: str
    maintainer: str
    maintainer_email: str
    notes: str
    licensce_id: str
    type: str
    owner_org: str
    creator_user_id: str
    metadata_created: datetime.datetime
    metadata_modified: datetime.datetime
    private: bool
    state: str

    package_tags: Query["PackageTag"]

    text_search_fields: List[str] = ...
    def __init__(self, **kw: Any) -> None: ...
    @classmethod
    def search_by_name(cls, text_query: str) -> Query["Package"]: ...
    @classmethod
    def get(
        cls, reference: str, for_update: bool = ...
    ) -> Optional["Package"]: ...
    @property
    def resources(self) -> List["Resource"]: ...
    def related_packages(self) -> List["Package"]: ...
    def add_resource(
        self,
        url: str,
        format: str = ...,
        description: str = ...,
        hash: str = ...,
        **kw: Any
    ) -> None: ...
    def add_tag(self, tag: "PackageTag") -> None: ...
    def add_tags(self, tags: List["PackageTag"]) -> None: ...
    def add_tag_by_name(
        self,
        tag_name: str,
        vocab: Optional["Vocabulary"] = ...,
        autoflush: bool = ...,
    ): ...
    def get_tags(self, vocab: "Vocabulary" = ...) -> List["PackageTag"]: ...
    def remove_tag(self, tag: "PackageTag"): ...
    def isopen(self) -> bool: ...
    def get_average_rating(self) -> Optional[float]: ...
    def as_dict(
        self, ref_package_by: str = ..., ref_group_by: str = ...
    ) -> Dict: ...
    def add_relationship(
        self, type_: str, related_package: "Package", comment: str = ...
    ): ...
    def get_relationships(
        self,
        with_package: Optional["Package"] = ...,
        type: Optional[str] = ...,
        active: bool = ...,
        direction: str = ...,
    ) -> "PackageRelationship": ...
    def get_relationships_with(
        self,
        other_package: "Package",
        type: Optional[str] = ...,
        active: bool = ...,
    ) -> "PackageRelationship": ...
    def get_relationships_printable(
        self,
    ) -> List[Tuple["Package", str, Optional[str]]]: ...
    @classmethod
    def get_license_register(cls) -> "LicenseRegister": ...
    @classmethod
    def get_license_options(cls) -> List[Tuple[str, str]]: ...
    def get_license(self) -> Optional["License"]: ...
    def set_license(self, license: Union["License", Dict]) -> None: ...
    license = ...
    def is_in_group(self, group: "Group") -> bool: ...
    def get_groups(
        self, group_type: Optional[str] = ..., capacity: Optional[str] = ...
    ) -> List["Group"]: ...
    def activity_stream_item(
        self, activity_type: str, user_id: str
    ) -> "Activity": ...
    def set_rating(
        self, user_or_ip: Union["User", str], rating: Union[int, str]
    ) -> None: ...

package_member_table: Table

class PackageMember(domain_object.DomainObject):
    package_id: str
    user_id: str
    capacity: str
    modified: datetime.datetime

class RatingValueException(Exception): ...