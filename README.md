# Geodescriber

Dynamically describe any geometry, from a geostore or valid geojson source.

## Run locally with docker

```bash
./geodescriber.sh develop
```

** Note you will need Geostore and ControlTower running too.

## Example of use

```python
import requests

#url = "http://localhost:4500/api/v1/geodescriber"
url = "https:/api.skydipper.com/v1/geodescriber"
params = {"geostore":"4dbc95a052c9c69e4d09fe72c359a207",
          "template":"False",
          "app":"skydipper"}
response = requests.get( url, params=params)
print(response.json())
```

Response:

```json
{
  "attributes": {
    "description": "The region is made up of different habitats, including Central Tibetan Plateau alpine steppe, and Upper Gangetic Plains moist deciduous forests. This region contains some Intact Forest. The most common environmental conditions of the area are polar tundra climate. The region is made up of several types of biomes, including Montane Grasslands and Shrublands, and Tropical and Subtropical Moist Broadleaf Forests. The location is predominantly land area. Area of 89.13Mha located in a mix of lowland and mountainous areas. ",
    "description_params": {},
    "lang": "en",
    "stats": {
      "biome": {
        "1": 590050.1372549013,
        "10": 661711.1098039213,
        "11": 60660.48627450982,
        "2": 141063.1137254899,
        "3": 59018.08627450981,
        "4": 53427.23529411764,
        "5": 39747.74117647059,
        "7": 60990.43529411765
      },
      "ecoregion": {
        "0": 61039.156862745105,
        "228": 10256.403921568624,
        "233": 64293.717647058824,
        "238": 168972.44705882348,
        "287": 346527.56862745073,
        "292": 129320.10980392131,
        "296": 11743.003921568641,
        "302": 59018.08627450981,
        "306": 37954.03921568627,
        "308": 15473.196078431372,
        "309": 16138.741176470594,
        "310": 23597.0,
        "311": 60990.43529411765,
        "750": 369673.6901960783,
        "751": 109407.09411764704,
        "768": 30617.97647058827,
        "769": 81752.99607843139,
        "770": 69892.68235294118
      },
      "intact2016": {
        "0": 1664091.1019607824,
        "1": 2577.243137254902
      },
      "isMountain": {
        "0": 749681.9176470579,
        "1": 916986.42745098
      },
      "koppen": {
        "14": 6058.329411764704,
        "26": 7900.658823529412,
        "27": 57794.07450980384,
        "34": 123923.18823529393,
        "37": 646801.6980392153,
        "38": 92012.6470588235,
        "50": 5041.0,
        "51": 52806.02352941179,
        "62": 674330.725490196
      },
      "seaLandFreshwater": {
        "0": 1649967.952941175,
        "2": 16700.392156862745
      }
    },
    "title": "Area near Nepal, Asia",
    "title_params": {}
  },
  "id": null,
  "type": "geodescriber"
}
```

## Auto-translate

Use language codes to return description in language of choice.

```python
import requests
url = "https:/api.skydipper.com/v1/geodescriber"
params = {"geostore":"4dbc95a052c9c69e4d09fe72c359a207",
          "template":"False",
          "app":"skydipper",
          "lang":'es'}
response = requests.get( url, params=params)
print(response.json())
```

Response:

```json
{
  "attributes": {
    "description": "La región se compone de diferentes hábitats, incluyendo Central Tibetana meseta esteparia alpino, y Alta llanuras del Ganges Bosques Húmedos de hoja caduca. Esta región contiene un poco de bosque intacto. Las mayoría de las condiciones ambientales comunes de la zona son el clima de la tundra polar. La región se compone de varios tipos de biomas, incluyendo Montano pastizales y matorrales, y tropicales y subtropicales húmedos de hoja ancha bosques. La ubicación es predominantemente la superficie terrestre. Área de 89.13Mha situada en una mezcla de tierras bajas y zonas montañosas.",
    "description_params": {},
    "lang": "es",
    "stats": {
      "biome": {
        "1": 590050.1372549013,
        "10": 661711.1098039213,
        "11": 60660.48627450982,
        "2": 141063.1137254899,
        "3": 59018.08627450981,
        "4": 53427.23529411764,
        "5": 39747.74117647059,
        "7": 60990.43529411765
      },
      "ecoregion": {
        "0": 61039.156862745105,
        "228": 10256.403921568624,
        "233": 64293.717647058824,
        "238": 168972.44705882348,
        "287": 346527.56862745073,
        "292": 129320.10980392131,
        "296": 11743.003921568641,
        "302": 59018.08627450981,
        "306": 37954.03921568627,
        "308": 15473.196078431372,
        "309": 16138.741176470594,
        "310": 23597.0,
        "311": 60990.43529411765,
        "750": 369673.6901960783,
        "751": 109407.09411764704,
        "768": 30617.97647058827,
        "769": 81752.99607843139,
        "770": 69892.68235294118
      },
      "intact2016": {
        "0": 1664091.1019607824,
        "1": 2577.243137254902
      },
      "isMountain": {
        "0": 749681.9176470579,
        "1": 916986.42745098
      },
      "koppen": {
        "14": 6058.329411764704,
        "26": 7900.658823529412,
        "27": 57794.07450980384,
        "34": 123923.18823529393,
        "37": 646801.6980392153,
        "38": 92012.6470588235,
        "50": 5041.0,
        "51": 52806.02352941179,
        "62": 674330.725490196
      },
      "seaLandFreshwater": {
        "0": 1649967.952941175,
        "2": 16700.392156862745
      }
    },
    "title": "Zona cercana a Nepal, Asia",
    "title_params": {}
  },
  "id": null,
  "type": "geodescriber"
}

```