CREATE TABLE IF NOT EXISTS weather_forecasts (
    city_id INT NOT NULL,
    dt BIGINT NOT NULL,
    temp NUMERIC(5, 2),
    feels_like NUMERIC(5, 2),
    pressure INT,
    humidity INT,
    wind_speed NUMERIC(5, 2),
    dt_txt VARCHAR(30),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    PRIMARY KEY (city_id, dt)
);