Item configuration
==================

    [item name]
    module      = "cmddemo"
    module_id   = 1
    type        = switch

- **[item name]**: is the human readable name of the item. This name has to be uniq and can only given ones within the hole item configruation file. Allowed Values: ***a-z, A-Z, 0-9, +, -, _***
- **module**: Is the name over which this item is addressable. The name has to be the same as the Class name of the module.
- **module_id**: is the module id which is used within the module class to adress the item itself.
- **type**: type defines what kind of item it is. Depending on this value you have different functions which are provided by this item. See [available modules defintion](modules.md) for more informations.
