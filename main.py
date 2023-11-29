from microbit import *
import maqueen

# 마퀸 모터 초기화
mq = maqueen.Motor()

while True:
    # 왼쪽과 오른쪽 라인 센서 읽기
    left_sensor = maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT)
    right_sensor = maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT)

    # 두 센서 모두 라인 위에 있을 때
    if left_sensor == 1 and right_sensor == 1:
        mq.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 50)
    
    # 왼쪽 센서만 라인 위에 있을 때
    elif left_sensor == 1 and right_sensor == 0:
        mq.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50)
        mq.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
    
    # 오른쪽 센서만 라인 위에 있을 때
    elif left_sensor == 0 and right_sensor == 1:
        mq.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)
        mq.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)

    # 라인을 잃어버렸을 때
    else:
        mq.motor_stop(maqueen.Motors.ALL)
