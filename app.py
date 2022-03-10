from flask import Flask
import ghhops_server as hs

# register hops app as middleware
app = Flask(__name__)
hops = hs.Hops(app)

# Controller-1
@app.route("/demo", methods=['GET'])
def get_demo():
    return "This is a demo api"

@hops.component(
    "/pointat",
    name="PointAt",
    description="Get point along curve",
    icon="examples/pointat.png",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("t", "t", "Parameter on Curve to evaluate"),
    ],
    outputs=[
        hs.HopsPoint("P", "P", "Point on curve at t")
    ]
)
def pointat(curve, t):
    return curve.PointAt(t)

if __name__ == "__main__":
    app.run()