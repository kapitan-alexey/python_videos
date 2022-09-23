#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from db_client import get_post, update_post_status
from telegram_client import post_video

post_to_post = get_post()

post_is_posted = post_video(post_to_post)

if post_is_posted:
    update_post_status(post_to_post)
