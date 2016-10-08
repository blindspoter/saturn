#!/usr/bin/env python
# -*- coding:utf-8 -*-

from plan import Plan as _Plan


class Plan(_Plan):
    '''
    定时任务定制
    '''
    pass


monitor_cron = Plan('monitor')
monitor_cron.script('-m crons.monitor', every='5.minute')


def main():
    monitor_cron.run('update')


if __name__ == '__main__':
    main()
