CREATE TABLE IF NOT EXISTS weather_forecasts (
    city_id INT NOT NULL,
    dt BIGINT NOT NULL,
    sunrise BIGINT,
    sunset BIGINT,
    temp_day NUMERIC(5, 2),
    temp_min NUMERIC(5, 2),
    temp_max NUMERIC(5, 2),
    pressure INT,
    humidity INT,
    wind_speed NUMERIC(5, 2),
    clouds INT,
    rain NUMERIC(5, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    PRIMARY KEY (city_id, dt)
);