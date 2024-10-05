from flask import Flask, jsonify, request

from useragent_parser.integrations.flask import FlaskUserAgentMiddleware

app = Flask(__name__)
FlaskUserAgentMiddleware(app)


@app.route("/")
def user_agent_info():
    ua = request.user_agent
    return jsonify(
        {
            "browser": f"{ua.browser.name} {ua.browser.version}",
            "os": f"{ua.os.name} {ua.os.version}",
            "device": ua.device,
            "is_mobile": ua.is_mobile,
            "is_tablet": ua.is_tablet,
            "is_desktop": ua.is_desktop,
            "is_bot": ua.is_bot,
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
