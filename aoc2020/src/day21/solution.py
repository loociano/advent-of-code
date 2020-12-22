# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import List, Dict, Set


def part_one(foods: List[str]) -> int:
  """
  Returns
    Times ingredients without allergens appear.
  """
  allergen_to_ingredients = _find_ingredients_with_allergen(foods)
  ingredients_with_allergens = [value
                               for value in allergen_to_ingredients.values()]
  # Count occurrences of ingredients that do not contain allergens.
  count_ingredients = 0
  for food in foods:
    ingredient_list, allergen_list = food.split(' (contains ')
    ingredients = set(ingredient_list.split(' '))
    for ingredient in ingredients:
      if ingredient not in ingredients_with_allergens:
        count_ingredients += 1
  return count_ingredients


def part_two(foods: List[str]) -> str:
  """
  Returns:
    Comma separated, alphabetical list of ingredients that contain allergens.
  """
  allergen_to_ingredients = _find_ingredients_with_allergen(foods)
  allergens = [allergen for allergen in allergen_to_ingredients.keys()]
  allergens.sort()  # alphabetical allergens
  return ','.join([allergen_to_ingredients.get(allergen)
                   for allergen in allergens])


def _find_ingredients_with_allergen(foods: List[str]) -> Dict[str, str]:
  allergen_to_ingredients = {}  # holds candidate ingredients
  # First pass: populate index of allergens with candidate ingredients.
  for food in foods:
    ingredient_list, allergen_list = food.split(' (contains ')
    ingredients = set(ingredient_list.split(' '))
    allergens = allergen_list.rstrip(')').split(', ')
    for allergen in allergens:
      if allergen_to_ingredients.get(allergen) is None:
        allergen_to_ingredients[allergen] = ingredients
      else:
        allergen_to_ingredients[allergen] = \
          allergen_to_ingredients.get(allergen).intersection(ingredients)

  # Find single ingredient per allergen.
  while not _found_all_allergens(allergen_to_ingredients):
    for allergen, ingredients in allergen_to_ingredients.items():
      if len(ingredients) == 1:
        ingredient_with_allergen = list(ingredients)[0]
        for other_allergen, other_ingredients in allergen_to_ingredients.items():
          if other_allergen == allergen:
            continue
          if ingredient_with_allergen in other_ingredients:
            other_ingredients.remove(ingredient_with_allergen)

  # Flatten set of ingredients into single one.
  for allergen, ingredients in allergen_to_ingredients.items():
    allergen_to_ingredients[allergen] = list(ingredients)[0]
  return allergen_to_ingredients


def _found_all_allergens(allergen_to_ingredients: Dict[str, Set[str]]) -> bool:
  for allergen, ingredients in allergen_to_ingredients.items():
    if len(ingredients) > 1:
      return False
  return True