# -*- coding: utf-8 -*-
import os

from lettuce import step, world
from selenium import webdriver

import liveandletdie


@step(u'Given a web application based on (\w+) located at ([\w/.]+)')
def given_a_web_application_based_on_framework_located_at_path(step, framework, path):
    
    world.AppClass = getattr(liveandletdie, framework)
    world.path = os.path.join(os.path.dirname(__file__), '../../../sample_apps', path)


@step(u'When I launch that application wit the subcommand ([\w/.]*)')
def when_i_launch_that_application_wit_the_subcommand_subcommand(step, dev_appserver_path):
    
    port = 8001
    
    if dev_appserver_path:
        world.app = world.AppClass(dev_appserver_path, world.path, port=port)
    else:
        world.app = world.AppClass(world.path, port=port)
    
    world.app.start(kill=True)
    


@step(u"When I go to the app's url")
def when_i_go_to_the_app_s_url(step):
    world.browser.get(world.app.url)


@step(u'Then I see "(.*)"')
def then_i_see_text(step, text):
    page_text = world.browser.find_element_by_tag_name('body').text    
    assert text in page_text
    world.app.stop()
