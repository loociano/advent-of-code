import re

class Passport:
  def __init__(self):
    self.byr = None
    self.iyr = None
    self.eyr = None
    self.hgt = None
    self.hcl = None
    self.ecl = None
    self.pid = None
    self.cid = None

  def has_required_fields(self):
    return self.byr and self.iyr and self.eyr and self.hgt and self.hcl \
           and self.ecl and self.pid

  def is_valid(self) -> bool:
    return self._is_valid_byr() and self._is_valid_iyr() \
           and self._is_valid_eyr() and self._is_valid_hgt() \
           and self._is_valid_hcl() and self._is_valid_ecl() \
           and self._is_valid_pid()

  def _is_valid_byr(self) -> bool:
    return 1920 <= int(self.byr) <= 2002

  def _is_valid_iyr(self) -> bool:
    return 2010 <= int(self.iyr) <= 2020

  def _is_valid_eyr(self) -> bool:
    return 2020 <= int(self.eyr) <= 2030

  def _is_valid_hgt(self) -> bool:
    if 'cm' in self.hgt:
      return 150 <= int(self.hgt.split('cm')[0]) <= 193
    if 'in' in self.hgt:
      return 59 <= int(self.hgt.split('in')[0]) <= 76
    return False

  def _is_valid_hcl(self) -> bool:
    return re.match('^#[0-9a-f]{6}$', self.hcl) is not None

  def _is_valid_ecl(self) -> bool:
    return re.match('^(amb|blu|brn|gry|grn|hzl|oth)$', self.ecl) is not None

  def _is_valid_pid(self) -> bool:
    return re.match('^[0-9]{9}$', self.pid) is not None