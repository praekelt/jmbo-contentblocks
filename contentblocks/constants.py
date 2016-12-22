from django.conf import settings

# Provide a minimal default detail view
infoblock_layouts = [("detail", "Detail view")]


if hasattr(settings, "CONTENTBLOCKS") and "layouts" in settings.CONTENTBLOCKS:
    layout_names = [i[0] for i in settings.CONTENTBLOCKS["layouts"]]
    if "detail" in layout_names:
        infoblock_layouts = settings.CONTENTBLOCKS["layouts"][:]
    else:
        infoblock_layouts.extend(settings.CONTENTBLOCKS["layouts"][:])

