"""
The Sims 4 Community Library is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode

Copyright (c) COLONOLNUTTY
"""
from sims4communitylib.modinfo import ModInfo
from sims4communitylib.services.common_service import CommonService
from sims4communitylib.testing.common_assertion_utils import CommonAssertionUtils
from sims4communitylib.testing.common_test_service import CommonTestService


class _TestService(CommonService):
    pass


class _TestSubService(_TestService):
    pass


# noinspection PyMissingOrEmptyDocstring
@CommonTestService.test_class(ModInfo.get_identity().name)
class CommonServiceTests:
    @staticmethod
    @CommonTestService.test()
    def _get_and_new_should_be_same_instance() -> None:
        CommonAssertionUtils.is_true(_TestService() is _TestService.get())

    @staticmethod
    @CommonTestService.test()
    def _get_and_new_should_equal_same_instance() -> None:
        CommonAssertionUtils.are_equal(_TestService(), _TestService.get())

    @staticmethod
    @CommonTestService.test()
    def _sub_service_should_be_separate_instance_from_parent() -> None:
        CommonAssertionUtils.is_false(_TestSubService.get() is _TestService.get())
