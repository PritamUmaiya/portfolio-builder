CREATE TABLE user (
    id INTEGER PRIMARY KEY,
    fname TEXT NOT NULL,
    lname TEXT,
    email TEXT NOT NULL,
    password TEXT NOT NULL,  -- Hashed
    avatar TEXT,
    bio TEXT,
    profession TEXT,
    works_at TEXT,
    studing_in TEXT,
    lives_in TEXT,
    public_email TEXT,  -- Visible in profile
    phone TEXT,
    link TEXT,
    about TEXT,
    secondary_btn TEXT NOT NULL DEFAULT 'contact',  -- (cv/resume/contact)
    secondary_btn_link TEXT NOT NULL DEFAULT '#contact',
    -- Social Media & links
    facebook TEXT,
    instagram TEXT,
    threads TEXT,
    twitter_x TEXT,
    linkedin TEXT,
    github TEXT,
    gitlab TEXT,
    youtube TEXT,
    twitch TEXT,
    medium TEXT,
    behance TEXT,
    dribble TEXT
);

CREATE TABLE portfolio (
    id INTEGER PRIMARY KEY,
    image TEXT NOT NULL,
    title TEXT,
    description TEXT,
    link TEXT
);

CREATE TABLE education (
    id INTEGER PRIMARY KEY,
    qualification TEXT NOT NULL,
    school TEXT,
    start_date TEXT,
    end_date TEXT
);

CREATE TABLE experiences (
    id INTEGER PRIMARY KEY,
    work TEXT NOT NULL,
    work_place TEXT,
    start_date TEXT,
    end_date TEXT
);

CREATE TABLE achievements (
    id INTEGER PRIMARY KEY,
    achievement TEXT NOT NULL,
    associated TEXT,
    year TEXT
);

CREATE TABLE certifications (
    id INTEGER PRIMARY KEY,
    certification TEXT NOT NULL,
    associated TEXT,
    year TEXT,
    credential TEXT,
    link TEXT
);

CREATE TABLE skills (
    id INTEGER PRIMARY KEY,
    skill TEXT NOT NULL
);

CREATE TABLE inbox (
    id INTEGER PRIMARY KEY,
    fname TEXT NOT NULL,
    lname TEXT,
    email TEXT NOT NULL,
    subject TEXT NOT NULL,
    message TEXT NOT NULL
);
