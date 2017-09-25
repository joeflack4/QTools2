    @staticmethod
    def get_gi_integrity(wb, sheetname):
        # Setp 1 - Duplicate GI's within a given list.
        # Step 1.a - Make conditional to check only if it is list1_name -> facility_name (sp).
        # Step 1.b - Make conditional to check only within that list.
        # Step 2 - Make several different functions and add calls for the following checks: missing parent,
        # missing child, invalid characters, etc. Change name of this function.
        dups = []
        try:
            choices = wb.sheet_by_name(sheetname)
            lists = Xlsform.get_column(choices, LIST_NAME)
            names = Xlsform.get_column(choices, NAME)
            d = {}
            for i, tup in enumerate(zip(lists, names)):
                if i == 0:
                    continue
                l, n = tup
                if l and l in d:
                    if n in d[l]:
                        dups.append((i, l, n))
                    else:
                        d[l].add(n)
                else:
                    d[l] = {n}
        except xlrd.XLRDError:
            # sheet not found
            pass
        except ValueError:
            # list_name, name not found
            pass

        # return dups
        return []
