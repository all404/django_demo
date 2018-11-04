from rest_framework.renderers import JSONRenderer


# 自定义JSONRenderer,使用utf-8
# 然后在配置文件中配置默认响应渲染类
class DRFJSONRenderer(JSONRenderer):
    charset = "utf-8"
