CREATE TABLE user (
    id INTEGER PRIMARY KEY,
    fname TEXT NOT NULL,
    lname TEXT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,  -- Hashed
    avatar TEXT,
    bio TEXT,
    profession TEXT,
    works_at TEXT,
    studies_at TEXT,
    hometown TEXT,
    public_email TEXT,  -- Visible in profile
    phone TEXT,
    link TEXT,
    about TEXT,
    file_url TEXT, -- (cv/resume link)
    file_type TEXT, -- (cv/resume)
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
    user_id INTEGER NOT NULL,
    image TEXT NOT NULL,
    title TEXT,
    description TEXT,
    link TEXT,
    FOREIGN KEY(user_id) REFERENCES user(id)
);

CREATE TABLE education (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    qualification TEXT NOT NULL,
    school TEXT,
    start_date TEXT,
    end_date TEXT,
    FOREIGN KEY(user_id) REFERENCES user(id)
);

CREATE TABLE experiences (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    work TEXT NOT NULL,
    work_place TEXT,
    start_date TEXT,
    end_date TEXT,
    FOREIGN KEY(user_id) REFERENCES user(id)
);

CREATE TABLE achievements (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    achievement TEXT NOT NULL,
    associated TEXT,
    year TEXT,
    FOREIGN KEY(user_id) REFERENCES user(id)
);

CREATE TABLE certifications (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    certification TEXT NOT NULL,
    associated TEXT,
    year TEXT,
    credential TEXT,
    link TEXT,
    FOREIGN KEY(user_id) REFERENCES user(id)
);

CREATE TABLE skills (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    skill TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES user(id)
);

CREATE TABLE inbox (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    fname TEXT NOT NULL,
    lname TEXT,
    email TEXT NOT NULL,
    subject TEXT NOT NULL,
    message TEXT NOT NULL,
    seen INTEGER NOT NULL DEFAULT 0, -- 1 for SEEN
    FOREIGN KEY(user_id) REFERENCES user(id)
);
