main = lambda data: data["bootstrap_distribution"] in ['k3s'] and data.get("addon_system_upgrade_controller", {}).get("enabled", False) == True
