CREATE VIEW tutorial_icustays AS
SELECT *
FROM (
    SELECT i.subject_id, i.hadm_id, i.stay_id, i.first_careunit, i.intime, i.outtime, i.los, p.gender, p.anchor_age, p.anchor_year, p.dod
	FROM icustays i
	LEFT JOIN patients p
	ON p.subject_id = i.subject_id
		AND (i.first_careunit IN ('Coronary Care Unit (CCU)', 'Medical Intensive Care Unit (MICU)', 'Medical/Surgical Intensive Care Unit (MICU/SICU)'))) m
WHERE gender IS NOT NULL
ORDER BY RAND()
LIMIT 100;

CREATE VIEW tutorial_labevents AS
SELECT labevents.subject_id, 
		labevents.hadm_id, 
        labevents.charttime, 
        labevents.itemid,
        labevents.value
FROM labevents 
RIGHT JOIN tutorial_icustays 
ON labevents.hadm_id = tutorial_icustays.hadm_id
	AND itemid IN (51301, 51279, 51222, 51221, 51265, 50878, 50861, 50912, 50983, 50971, 50902, 50882, 50820, 51265)
    AND tutorial_icustays.intime <= labevents.charttime 
    AND DATEADD(hour, 24, tutorial_icustays.intime)  >= labevents.charttime;

CREATE VIEW tutorial_chartevents AS
SELECT c.subject_id, c.hadm_id, c.stay_id, c.charttime, c.itemid, c.value
FROM chartevents c
RIGHT JOIN tutorial_icustays 
ON c.hadm_id = tutorial_icustays.hadm_id
	AND c.itemid IN (220209, 220210, 220210, 220045, 223762, 220277)
    AND tutorial_icustays.intime <= c.charttime 
    AND DATEADD(hour, 24, tutorial_icustays.intime) >= c.charttime 
