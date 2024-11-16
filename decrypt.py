import cryptpandas as crp

decrypted_df = crp.read_encrypted(
    path="release_3547.crypt", password="oUFtGMsMEEyPCCP6"
)


print(decrypted_df)
