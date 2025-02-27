# -*- coding: utf-8 -*-

# Standard library imports
from __future__ import unicode_literals

# Third party imports
from django.conf import settings

# Local application / specific library imports


# General
MACHINA_FORUM_NAME = getattr(settings, 'MACHINA_FORUM_NAME', 'Machina')
MACHINA_MARKUP_LANGUAGE = getattr(settings, 'MACHINA_MARKUP_LANGUAGE', ('django_markdown.utils.markdown', {}))
MACHINA_MARKUP_WIDGET = getattr(settings, 'MACHINA_MARKUP_WIDGET', 'django_markdown.widgets.MarkdownWidget')


# Forum
FORUM_IMAGE_UPLOAD_TO = getattr(settings, 'MACHINA_FORUM_IMAGE_UPLOAD_TO', 'machina/forum_images')
FORUM_IMAGE_WIDTH = getattr(settings, 'MACHINA_FORUM_IMAGE_WIDTH', 100)
FORUM_IMAGE_HEIGHT = getattr(settings, 'MACHINA_FORUM_IMAGE_HEIGHT', 70)

DEFAULT_FORUM_IMAGE_SETTINGS = {
    'width': FORUM_IMAGE_WIDTH,
    'height': FORUM_IMAGE_HEIGHT
}

FORUM_TOPICS_NUMBER_PER_PAGE = getattr(settings, 'MACHINA_FORUM_TOPICS_NUMBER_PER_PAGE', 20)


# Conversation
TOPIC_ANSWER_SUBJECT_PREFIX = getattr(settings, 'MACHINA_TOPIC_ANSWER_SUBJECT_PREFIX', 'Re:')

TOPIC_POSTS_NUMBER_PER_PAGE = getattr(settings, 'MACHINA_TOPIC_POSTS_NUMBER_PER_PAGE', 15)
TOPIC_REVIEW_POSTS_NUMBER = getattr(settings, 'MACHINA_TOPIC_REVIEW_POSTS_NUMBER', 10)


# Polls
POLL_MAX_OPTIONS_PER_USER = getattr(settings, 'MACHINA_POLL_MAX_OPTIONS_PER_USER', 10)


# Attachments
ATTACHMENT_FILE_UPLOAD_TO = getattr(settings, 'MACHINA_ATTACHMENT_FILE_UPLOAD_TO', 'machina/attachments')
ATTACHMENT_CACHE_NAME = getattr(settings, 'MACHINA_ATTACHMENT_CACHE_NAME', 'machina_attachments')


# Member
PROFILE_AVATAR_UPLOAD_TO = getattr(settings, 'MACHINA_PROFILE_AVATAR_UPLOAD_TO', 'machina/avatar_images')

PROFILE_AVATAR_WIDTH = getattr(settings, 'MACHINA_PROFILE_AVATAR_WIDTH', 150)
PROFILE_AVATAR_HEIGHT = getattr(settings, 'MACHINA_PROFILE_AVATAR_HEIGHT', 250)
PROFILE_AVATAR_MIN_WIDTH = getattr(settings, 'MACHINA_PROFILE_AVATAR_MIN_WIDTH', None)
PROFILE_AVATAR_MAX_WIDTH = getattr(settings, 'MACHINA_PROFILE_AVATAR_MAX_WIDTH', None)
PROFILE_AVATAR_MIN_HEIGHT = getattr(settings, 'MACHINA_PROFILE_AVATAR_MIN_HEIGHT', None)
PROFILE_AVATAR_MAX_HEIGHT = getattr(settings, 'MACHINA_PROFILE_AVATAR_MAX_HEIGHT', None)
PROFILE_AVATAR_MAX_UPLOAD_SIZE = getattr(settings, 'MACHINA_PROFILE_AVATAR_MAX_UPLOAD_SIZE', 0)

DEFAULT_AVATAR_SETTINGS = {
    'width': PROFILE_AVATAR_WIDTH,
    'height': PROFILE_AVATAR_HEIGHT,
    'min_width': PROFILE_AVATAR_MIN_WIDTH,
    'max_width': PROFILE_AVATAR_MAX_WIDTH,
    'min_height': PROFILE_AVATAR_MIN_HEIGHT,
    'max_height': PROFILE_AVATAR_MAX_HEIGHT,
    'max_upload_size': PROFILE_AVATAR_MAX_UPLOAD_SIZE
}

PROFILE_SIGNATURE_MAX_LENGTH = getattr(settings, 'MACHINA_PROFILE_SIGNATURE_MAX_LENGTH', 255)

PROFILE_RECENT_POSTS_NUMBER = getattr(settings, 'MACHINA_PROFILE_RECENT_POSTS_NUMBER', 15)


# Permission
DEFAULT_AUTHENTICATED_USER_FORUM_PERMISSIONS = getattr(
    settings, 'MACHINA_DEFAULT_AUTHENTICATED_USER_FORUM_PERMISSIONS', [])
