#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from db_client import get_video, update_video_status
from telegram_client import post_video

video_to_post = get_video()

video_is_posted = post_video(video_to_post)

if video_is_posted:
    update_video_status(video_to_post)
