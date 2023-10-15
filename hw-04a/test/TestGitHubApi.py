"""
Author: Russ Harrington
"""


import unittest
from unittest import mock
from unittest.mock import MagicMock, patch
import json

from GitHubApi import PrintUserCommitsCountsPerRepo
from GitHubApi import GetListOfRepos
from GitHubApi import GetRepoCommitCounts
from GitHubApi import GetGithubCommitsFromRepo
from GitHubApi import GetGithubUserRepositoryList


def is_json(myjson):
    """Helper function to determine valid json
    """
    try:
        json.dumps(myjson)
    except ValueError:
        return False
    return True


class TestGitHubApi(unittest.TestCase):


    @patch('GitHubApi.requests')
    def testGetUserRepositoryInfo(self, mock_requests):
        """
        Test a valid user returns 
        """
        mock_reponse = MagicMock()
        mock_reponse.status_code = 200
        mock_reponse.text = '[{\"name\": \"repo1\"}]'
        mock_requests.get.return_value = mock_reponse

        self.assertGreaterEqual(len(PrintUserCommitsCountsPerRepo("RussJH")), 1)

    @patch('GitHubApi.requests')
    def testGetUserRepositoryInfoInvalidUser(self, mock_requests):
        """
        Invalid user data should return an empty string
        """
        mock_reponse = MagicMock()
        mock_reponse.status_code = 200
        mock_reponse.text = '[ ]'
        mock_requests.get.return_value = mock_reponse
        self.assertEqual(len(PrintUserCommitsCountsPerRepo("")), 0)

    def testGetListOfRepos(self):
        # test repos
        json_data = json.loads('[{\"name\": \"repo1\"},{\"name\": \"repo2\"},{\"name\": \"repo3\"}]')
        repo_list = ['repo1','repo2', 'repo3']
        self.assertEqual(GetListOfRepos(json_data), repo_list)

    def testGetListOfReposEmptySet(self):
        # test empty set
        json_data = json.loads('[]')
        self.assertEqual(GetListOfRepos(json_data), [])

    def testGetListOfReposInvalidJson(self):
        # test invalid json
        self.assertEqual(GetListOfRepos("String data"), [])

    def testRepoCommitCounts(self):
        # test valid
        json_data = json.loads('[ {\"sha\" : \"888fff\", \"commit\":{ \"comment_count\" : 0} },{\"sha\" : \"888fff\", \"commit\":{ \"comment_count\" : 0}}]')
        self.assertEqual(GetRepoCommitCounts(json_data), 2)

    def testRepoCommitCountsZero(self):
        """ test empty set """
        json_data = json.loads('[]')
        self.assertEqual(GetRepoCommitCounts(json_data), 0)

    def testRepoCommitCountsInvalid(self):
        # test invalid json
        self.assertEqual(GetRepoCommitCounts("INVALID JSON"), 0)

    @patch('GitHubApi.requests')
    def testGetGithubUserRepositoryList(self, mock_requests):
        #test valid json return
        mock_reponse = MagicMock()
        mock_reponse.status_code = 200
        mock_reponse.text = '[{\"name\": \"repo1\"}]'
        mock_requests.get.return_value = mock_reponse
        self.assertTrue(is_json(GetGithubUserRepositoryList("RussJH")))

    @patch('GitHubApi.requests')
    def testGetGithubUserRepositoryListInvalid(self, mock_requests):
        #test valid json return
        mock_reponse = MagicMock()
        mock_reponse.status_code = 200
        mock_reponse.text = '[ ]'
        mock_requests.get.return_value = mock_reponse
        self.assertTrue(is_json(GetGithubUserRepositoryList("")))

    @patch('GitHubApi.requests')
    def testGetGithubCommitsFromRepo(self, mock_requests):
        #test valid json data
        mock_reponse = MagicMock()
        mock_reponse.status_code = 200
        mock_reponse.text = '[ {\"sha\" : \"888fff\", \"commit\":{ \"comment_count\" : 0} }]'
        mock_requests.get.return_value = mock_reponse
        self.assertTrue(is_json(GetGithubCommitsFromRepo("RussJH","SSW-567")))

    @patch('GitHubApi.requests')
    def testGetGithubCommitsFromRepoInvalid(self, mock_requests):
        #test valid json data
        mock_reponse = MagicMock()
        mock_reponse.status_code = 200
        mock_reponse.text = '[ ]'
        mock_requests.get.return_value = mock_reponse
        self.assertTrue(is_json(GetGithubCommitsFromRepo("RussJH","NOT_MY_REPO")))
