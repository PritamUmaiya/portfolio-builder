CREATE TABLE user (
    fname TEXT NOT NULL,
    lname TEXT,
    email TEXT NOT NULL,
    password TEXT NOT NULL, -- Hashed
    avatar TEXT,
    bio TEXT,
    profession TEXT,
    public_email TEXT, -- Visible in profile
    secondary_btn TEXT NOT NULL  -- (cv/resume/contact)
);

CREATE TABLE links (
    id INTEGER NOT NULL PRIMARY KEY,
    site TEXT NOT NULL,
    url TEXT NOT NULL
);

CREATE INDEX idx_links_id ON links(id);

CREATE TABLE portfolio (
    id INTEGER NOT NULL PRIMARY KEY,
    image TEXT NOT NULL,
    title TEXT,
    description TEXT
);

CREATE INDEX idx_portfolio_id ON portfolio(id);
