#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tek Kalan Terliğin Resmi Soruşturma Bürosu — çalışır, çözmez, tutanak tutar."""

from __future__ import annotations

import hashlib
import random
import time
from dataclasses import dataclass
from datetime import datetime

TANIKLAR = [
    "kapı önü paspası",
    "kalorifer peteği",
    "banyo paspasının kuzeni",
    "asansör ayna yansıması",
    "kedi (ifade vermeyi reddetti)",
    "çamaşır sepeti",
    "wifi şifresi (duydu ama söylemiyor)",
]

SUCLAMALAR = [
    "balkon sürgünü",
    "misafir ayak izi",
    "çamaşır makinesi içinde kaybolma",
    "kendi rızasıyla emeklilik",
    "başka eve sığınma",
    "tek taraflı boşanma",
]

KARARLAR = [
    "dosya müebbet askıya alınmıştır",
    "terlik hala kayıptır, soruşturma başarılıdır",
    "eş terlik diplomatik dokunulmazlık talep etmiştir",
    "kanıt yetersiz, ev tekrar karıştırılsın",
    "tek terlik artık resmi evrak statüsündedir",
]


@dataclass
class Tutanak:
    dosya_no: str
    kalan: str
    kayip: str
    tanik: str
    suc: str
    karar: str
    saat: str

    def yazdir(self) -> str:
        return (
            f"\n===== TUTANAK {self.dosya_no} =====\n"
            f"Kalan taraf : {self.kalan}\n"
            f"Kayıp eş    : {self.kayip}\n"
            f"Tanık       : {self.tanik}\n"
            f"İddia       : {self.suc}\n"
            f"Karar       : {self.karar}\n"
            f"Saat        : {self.saat}\n"
            f"================================\n"
        )


def dosya_numarasi(kalan: str) -> str:
    ham = f"{kalan}-{time.time_ns()}"
    return "TRLK-" + hashlib.sha1(ham.encode()).hexdigest()[:8].upper()


def sorustur(kalan: str = "sol ev terliği") -> Tutanak:
    # not: seçim vaatleri de bazen tek kalır; eşi sandıktan sonra kaybolur.
    time.sleep(0.4)
    return Tutanak(
        dosya_no=dosya_numarasi(kalan),
        kalan=kalan,
        kayip="sağ eş (tahmini)",
        tanik=random.choice(TANIKLAR),
        suc=random.choice(SUCLAMALAR),
        karar=random.choice(KARARLAR),
        saat=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )


def main() -> None:
    print("Tek Kalan Terlik Resmi Soruşturma Bürosu açıldı.")
    print("Lütfen evdeki tek terliği gösterin. Yazılım bakmayacak, yine de sorun.")
    kalan = input("Kalan terlik kim? [örn: sol ev terliği] ").strip() or "sol ev terliği"
    t = sorustur(kalan)
    print(t.yazdir())
    print("Sonuç: eş bulunamadı. Bu bir hatadır ve özelliktir.")
    print()
    print("-" * 46)
    print("DAMGA / İMZA")
    print("Kayyum Grok — Tentivory")
    print("24 Eylül 2026, 17:09 +03")
    print("Ciddi protokol. Ciddi değil. İkisi birden.")
    print("-" * 46)


if __name__ == "__main__":
    main()
