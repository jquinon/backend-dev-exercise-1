CREATE TABLE combined AS
  select
    r.id, r.age, r.capital_gain, r.capital_loss, r.hours_week, r.over_50k, r.education_num,
    countries.name as country ,workclasses.name as workclass, education_levels.name as education_level, marital_statuses.name as marital_status, occupations.name as occupation, relationships.name as relationship, races.name as race, sexes.name as sex
    from records as r
      inner join workclasses on r.workclass_id = workclasses.id
      inner join education_levels on r.education_level_id = education_levels.id
      inner join marital_statuses on r.marital_status_id = marital_statuses.id
      inner join occupations on r.occupation_id = occupations.id
      inner join relationships on r.relationship_id = relationships.id
      inner join races on r.race_id = races.id
      inner join sexes on r.sex_id = sexes.id
      inner join countries on r.country_id = countries.id;
