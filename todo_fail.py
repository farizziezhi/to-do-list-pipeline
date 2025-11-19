def hapus_kegiatan ( kegiatan , kegiatan_hapus):
    if 0 <= kegiatan_hapus < len(kegiatan):
        return kegiatan.pop(kegiatan_hapus)
    return None