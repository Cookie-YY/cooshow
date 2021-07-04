def get_custom_apis(results, format_pool_custom):
    file = results.get("file")
    from settings import PROJECT
    file = file.split(".")[0]
    project_settings = __import__(f"settings.{PROJECT}.custom.{file}", globals(), locals(),
                                  ["run"])  # 导入前端配置

    run = project_settings.run

    code, msg, data = run(**format_pool_custom)
    return code, msg, data