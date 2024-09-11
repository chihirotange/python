import json

with open("inu_identities.json") as f:
    data = json.load(f)

assets = ["clothing", "hand", "hat"]


new_data = []
for i in data:
    indi_data = {
        "id" : "INU_" + str(i["id"]).zfill(5),
    }

    current_set = None
    is_fullset = True
    for __ in i["attributes"]:
        asset_trait = __.split("_")[0]

        if asset_trait in assets:
            if asset_trait == "clothing":
                converted = "Cloth"
            if asset_trait == "hand":
                converted = "Hands"
            if asset_trait == "hat":
                converted = "Accessories"
            
            asset_value = __.split("_")[1]
            if current_set == None:
                current_set = asset_value
            
            if current_set == asset_value:
                pass
            else:
                is_fullset = False
            if asset_value == "none":
                asset_value = None
            try:
                indi_data[asset_trait] = "INU_" + asset_value[0].upper() + asset_value[1:] + "_" + converted
            except:
                continue

        if asset_trait in ["canis","bioz", "cyborg", "cosmic"]:
            fur_color = __.split("_")[1]
            indi_data["sub-race"] = "INU_" + asset_trait.title()
            indi_data["fur color"] = fur_color[0].upper() + fur_color[1:]

        if asset_trait == "eye":
            indi_data["eye color"] = __.split("_")[1][0].upper() + __.split("_")[1][1:]
    if is_fullset == True:
        indi_data["special"] = "full-set"
    new_data.append(indi_data)

with open("fixed_metadata.json", "w") as f:
    json.dump(new_data,f, indent=2)