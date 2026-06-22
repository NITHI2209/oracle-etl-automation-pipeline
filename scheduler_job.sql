BEGIN
   DBMS_SCHEDULER.CREATE_JOB (
      job_name        => 'MOVE_HISTORY_JOB',
      job_type        => 'STORED_PROCEDURE',
      job_action      => 'MOVE_TO_HISTORY',
      start_date      => SYSTIMESTAMP,
      repeat_interval => 'FREQ=DAILY;BYHOUR=12;BYMINUTE=0;BYSECOND=0',
      enabled         => TRUE
   );
END;
/