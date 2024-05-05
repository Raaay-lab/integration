DO $$
DECLARE
    current_date_variable TIMESTAMP;
BEGIN
    current_date_variable := NOW();
    RAISE NOTICE '(%)', current_date_variable;
	RAISE NOTICE '(%)', current_date_variable - interval '1 min';
END $$;