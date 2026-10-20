CREATE TABLE IF NOT EXISTS plans (
    id int GENERATED ALWAYS AS identity PRIMARY KEY,
    name varchar(100) NOT NULL UNIQUE,
    price numeric(10, 2) NOT NULL CHECK (price >= 0),
    quota int NOT NULL CHECK (quota >= 0),
    created_on timestamptz NOT NULL DEFAULT now(),
    updated_on timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS clients (
    id int GENERATED ALWAYS AS identity PRIMARY KEY,
    name varchar(255) NOT NULL,
    created_on timestamptz NOT NULL DEFAULT now(),
    updated_on timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS contracts (
    id int GENERATED ALWAYS AS identity PRIMARY KEY,
    start_date date NOT NULL,
    billing varchar(7) NOT NULL CHECK (billing IN ('monthly', 'annual')),
    status varchar(15) NOT NULL CHECK (status IN ('estimate', 'signed', 'active', 'suspended', 'terminated')),
    client_id int NOT NULL,
    plan_id int NOT NULL,
    created_on timestamptz NOT NULL DEFAULT now(),
    updated_on timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT fk_client FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE RESTRICT,
    CONSTRAINT fk_plan FOREIGN KEY (plan_id) REFERENCES plans(id) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS timesheets (
    id int GENERATED ALWAYS AS identity PRIMARY KEY,
    intervention_date date NOT NULL,
    duration int NOT NULL CHECK (duration >= 0),
    description varchar(255),
    contract_id int NOT NULL,
    created_on timestamptz NOT NULL DEFAULT now(),
    updated_on timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT fk_contract FOREIGN KEY (contract_id) REFERENCES contracts(id) ON DELETE RESTRICT
);

CREATE INDEX IF NOT EXISTS idx_contracts_client_id ON contracts (client_id);
CREATE INDEX IF NOT EXISTS idx_contracts_plan_id   ON contracts (plan_id);
CREATE INDEX IF NOT EXISTS idx_timesheets_contract_date
    ON timesheets (contract_id, intervention_date);

CREATE OR REPLACE FUNCTION set_updated_on()
RETURNS trigger AS $$
BEGIN
    NEW.updated_on = now();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_plans_updated_on ON plans;
CREATE TRIGGER trg_plans_updated_on
BEFORE UPDATE ON plans
FOR EACH ROW EXECUTE FUNCTION set_updated_on();

DROP TRIGGER IF EXISTS trg_clients_updated_on ON clients;
CREATE TRIGGER trg_clients_updated_on
BEFORE UPDATE ON clients
FOR EACH ROW EXECUTE FUNCTION set_updated_on();

DROP TRIGGER IF EXISTS trg_contracts_updated_on ON contracts;
CREATE TRIGGER trg_contracts_updated_on
BEFORE UPDATE ON contracts
FOR EACH ROW EXECUTE FUNCTION set_updated_on();

DROP TRIGGER IF EXISTS trg_timesheets_updated_on ON timesheets;
CREATE TRIGGER trg_timesheets_updated_on
BEFORE UPDATE ON timesheets
FOR EACH ROW EXECUTE FUNCTION set_updated_on();