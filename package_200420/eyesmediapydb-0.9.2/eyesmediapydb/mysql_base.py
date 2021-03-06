# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import logging
import traceback
import pymysql
from eyesmediapydb import DefaultDBConfig

logger = logging.getLogger("eyesmediapydb")


class MySqlConfig(DefaultDBConfig):
    __charset = "utf8mb4"

    @property
    def charset(self):
        return self.__charset

    @charset.setter
    def charset(self, value):
        self.__charset = value


class MySqlConnectionProvider(object):

    def __init__(self, config):
        if not isinstance(config, MySqlConfig):
            raise Exception("input attribute(config) type must be mysql_base.MySqlConfig")
        self.mysql_config = config

    def open_connection(self):
        connection = pymysql.connect(
            host=self.mysql_config.host,
            user=self.mysql_config.username,
            port=self.mysql_config.port,
            passwd=self.mysql_config.password,
            db=self.mysql_config.dbname,
            charset=self.mysql_config.charset,
            cursorclass=pymysql.cursors.DictCursor
        )
        logger.debug("open connection:{}".format(connection))
        return connection

    def close_connection(self, connection):
        try:
            if connection is not None:
                connection.close()
                logger.debug("connection({}) closed:{}".format(connection, connection._closed))
        except:
            logger.error(traceback.format_exc())
