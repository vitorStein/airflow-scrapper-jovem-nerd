import requests
import pandas as pd

import time


def main():
    data = []
    page_number = 0

    while True:
        link_base = f"https://jovemnerd.com.br/wp-json/jovemnerd/v1/nerdcasts/?offset=0&page={page_number}&per_page=50&paginated=false"
        response = requests.get(link_base)

        if response.json()["data"] == []:
            break

        data.extend(response.json()["data"])
        time.sleep(1)
        page_number += 1

    df = pd.DataFrame(data)

    df.drop("thumbnails", axis="columns", inplace=True)
    df.drop("insertions", axis="columns", inplace=True)

    df = df[
        [
            "id",
            "url",
            "published_at",
            "duration",
            "title",
            "episode",
            "product",
            "subject",
            "description",
            "guests",
        ]
    ]

    for index, row in df.iterrows():
        try:
            description_clean = (
                row["description"].replace("<p>", "").replace("</p>", "")
            )
            df.at[index, "description"] = description_clean
        except:
            print(row["description"])

    df.to_csv("/home/var/data/data.csv", index=False)


if __name__ == "__main__":
    main()
