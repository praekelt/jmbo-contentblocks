from django.conf import settings

# Provide a minimal default detail view
infoblock_layouts = [("detail", "Detail view")]


if hasattr(settings, "CONTENTBLOCKS") and "LAYOUTS" in settings.CONTENTBLOCKS:
    layout_names = [i[0] for i in settings.CONTENTBLOCKS["LAYOUTS"]]
    if "detail" in layout_names:
        infoblock_layouts = settings.CONTENTBLOCKS["LAYOUTS"][:]
    else:
        infoblock_layouts.extend(settings.CONTENTBLOCKS["LAYOUTS"][:])

