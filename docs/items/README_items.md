Item configuration
==================

    [item name]
    module_name = "cmddemo"
    module_addr = 1
    type        = switch

- **[item name]**: is the human readable name of the item. This name has to be uniq and can only given ones within the hole item configruation file. Allowed Values: ***a-z, A-Z, 0-9, +, -, _***
- **module_name**: Is the name over which this item is addressable. The name has to be the same as the Class name of the module.
- **module_addr**: is the module id which is used within the module class to adress the item itself.
- **type**: type defines what kind of item it is. Depending on this value you have different functions which are provided by this item. Reffer to [modules documentation](docs/modules/README_modules.md) for more informations.
