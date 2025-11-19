def test_tambah_kegiatan():
    daftar_kegiatan = []
    result = test_tambah_kegiatan(daftar_kegiatan, "Belajar CI")
    assert len(result) == 1

def test_SelaluGagal():
    assert False