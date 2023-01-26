--
-- Structure de la table `lists`
--

CREATE TABLE IF NOT EXISTS lists (
    "id" INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "name" TEXT NOT NULL,
    "display_name" TEXT NOT NULL
);

--
-- Structure de la table `publishers`
--

CREATE TABLE IF NOT EXISTS publishers (
    "id" INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "name" TEXT NOT NULL
);

--
-- Structure de la table `books`
--

CREATE TABLE IF NOT EXISTS books (
    "id" INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "title" TEXT NOT NULL,
    "description" TEXT,
    "author" TEXT,
    "contributor" TEXT,
    "publisher" TEXT,
    "amazon_product_url" TEXT,
    "bestsellers_date" DATE,
    "published_date" DATE,
    "list_id" INT NOT NULL REFERENCES lists("id"),
    "publisher_id" INT NOT NULL REFERENCES publishers("id")
);

--
-- Structure de la table `sellers`
--

CREATE TABLE IF NOT EXISTS sellers (
    "id" INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "name" TEXT NOT NULL
);

--
-- Structure de la table `sell_details`
--

CREATE TABLE IF NOT EXISTS sell_details (
    "id" INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "price" BIGINT NOT NULL,
    "symbol" TEXT,
    "seller_id" INT NOT NULL REFERENCES sellers("id"),
    "book_id" INT NOT NULL REFERENCES books("id")
);

--
-- Structure de la table `states`
--

CREATE TABLE IF NOT EXISTS states (
    "id" INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "name" TEXT
);

--
-- Structure de la table `counties`
--

CREATE TABLE IF NOT EXISTS counties (
    "id" INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "name" TEXT,
    "fips" TEXT,
    "state_id" INT REFERENCES states("id")
);

--
-- Structure de la table `covid`
--

CREATE TABLE IF NOT EXISTS covid (
    "id" INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "date" DATE,
    "cases" INT,
    "deaths" INT,
    "state_id" INT REFERENCES states("id"),
    "county_id" INT REFERENCES counties("id")
);
