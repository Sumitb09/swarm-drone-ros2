#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Pose

from flask import Flask, render_template_string
from flask_socketio import SocketIO

import threading

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

poses = {
    "leader": {"x": 0, "y": 0},
    "f1": {"x": 0, "y": 0},
    "f2": {"x": 0, "y": 0},
    "f3": {"x": 0, "y": 0},
}


HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Swarm Dashboard</title>

<script src="https://cdn.socket.io/4.7.2/socket.io.min.js"></script>

<style>
body{
background:black;
margin:0;
overflow:hidden;
}

canvas{
background:#111;
}
</style>

</head>

<body>

<canvas id="c"></canvas>

<script>

const socket = io();

const canvas = document.getElementById("c");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let swarm = {};

socket.on("update",(data)=>{
 swarm = data;
});

function draw(){

 ctx.clearRect(0,0,canvas.width,canvas.height);

 function drone(x,y,color){

   ctx.beginPath();
   ctx.arc(x,y,10,0,2*Math.PI);
   ctx.fillStyle=color;
   ctx.fill();
 }

 drone(
   swarm.leader?.x || 100,
   swarm.leader?.y || 100,
   "red"
 );

 drone(
   swarm.f1?.x || 50,
   swarm.f1?.y || 50,
   "green"
 );

 drone(
   swarm.f2?.x || 50,
   swarm.f2?.y || 50,
   "blue"
 );

 drone(
   swarm.f3?.x || 50,
   swarm.f3?.y || 50,
   "yellow"
 );

 requestAnimationFrame(draw);
}

draw();

</script>

</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)


class SwarmMonitor(Node):

    def __init__(self):
        super().__init__("swarm_monitor")

        self.create_subscription(
            Pose,
            "/leader_pose",
            self.leader_cb,
            10
        )

        self.create_subscription(
            Pose,
            "/follower1_pose",
            self.f1_cb,
            10
        )

        self.create_subscription(
            Pose,
            "/follower2_pose",
            self.f2_cb,
            10
        )

        self.create_subscription(
            Pose,
            "/follower3_pose",
            self.f3_cb,
            10
        )

    def leader_cb(self,msg):
        poses["leader"]["x"]=msg.position.x*3
        poses["leader"]["y"]=msg.position.y*3
        socketio.emit("update",poses)

    def f1_cb(self,msg):
        poses["f1"]["x"]=msg.position.x*3
        poses["f1"]["y"]=msg.position.y*3

    def f2_cb(self,msg):
        poses["f2"]["x"]=msg.position.x*3
        poses["f2"]["y"]=msg.position.y*3

    def f3_cb(self,msg):
        poses["f3"]["x"]=msg.position.x*3
        poses["f3"]["y"]=msg.position.y*3


def ros_thread():

    rclpy.init()

    node = SwarmMonitor()

    rclpy.spin(node)


if __name__ == "__main__":

    threading.Thread(
        target=ros_thread,
        daemon=True
    ).start()

    socketio.run(
        app,
        host="0.0.0.0",
        port=5000
    )
