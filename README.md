# dss-quiz5 – Perceptron Devam Çalışması

Model, tek katmanlı perceptron (ANN’in temel nöronu) ve gereğine uygun çalışıyor.

Epoch: Tüm eğitim örneklerinin bir kez baştan sona işlenmesi. 
Bu veri kümesinde 4 örnek var; 
dolayısıyla bir epoch = 4 iterasyon (ör. iteration5–8, 9–12, 13–16).

epoch_errors: İlgili epoch boyunca yapılan hatalı tahmin sayısı. 
Epoch başında 0’a sıfırlanır; her örnekte E ≠ 0 olduğunda 1 artırılır. 
Epoch sonunda epoch_errors == 0 ise eğitim durur.

Eğitim 16’da durdu çünkü durdurma kuralı epoch bazlı: 
bir epoch’un tamamı hata sayısı 0 olursa döngü, epoch bittiğinde duruyor. 
11–14 arasındaki ardışık dört E=0 iki farklı epoch’a yayılıyor (11–12 epoch 2, 13–14 epoch 3), 
bu yüzden durdurma tetiklenmiyor. 
İlk tamamen hatasız epoch, 13–16 arası (epoch 3). 
Kontrol epoch sonunda yapıldığı için döngü iteration16 tamamlandıktan sonra durdu.

Bu proje, verilen ağırlıklardan (iteration4 sonrası) başlayarak perceptron eğitimini iteration5'ten itibaren sürdürür. Dört ardışık E=0 elde edilene kadar (beklenen: iteration11–14) her adımı ve olası ağırlık güncellemelerini yazdırır. Sonunda X1=X2=X3=0.5 için tahmini döndürür.

## Çalıştırma
PowerShell tarzı ayraçla tek satırda çalıştırmak isterseniz:

```powershell
python .\perceptron_continue.py; echo "Done"
```

Veya tek komut:

```powershell
python .\perceptron_continue.py
```

## Beklenen Özet
- Dört ardışık sıfır hata: iteration11–iteration14
- Nihai ağırlıklar: W1=0.8, W2=-0.2, W3=-0.1
- X1=X2=X3=0.5 için: Net=0.25, Theta=0.5 => Y=0

