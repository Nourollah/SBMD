"""
# Author: Amir Masoud Nourollah

# SMILES Syntax Table
| Symbol/Feature       | Description                                  | Example             | Meaning                          |
|----------------------|----------------------------------------------|---------------------|----------------------------------|
| Atom                 | Elemental symbol (C, O, N, etc.)             | C                   | Methane (CH₄)                    |
| Single Bond          | Adjacent atoms or hyphen (-)                 | CC or C-C           | Ethane (CH₃-CH₃)                 |
| Double Bond          | Equals sign (=)                              | C=C                 | Ethene (CH₂=CH₂)                 |
| Triple Bond          | Hash sign (#)                                | C#C                 | Ethyne (HC≡CH)                   |
| Branch               | Parentheses () for substituents              | CC(C)C              | Isobutane (CH₃-CH(CH₃)-CH₃)      |
| Ring Closure         | Numbers (1, 2, etc.) to close rings          | C1CC1               | Cyclopropane (C₃H₆)              |
| Aromatic Atom        | Lowercase letters (c, n, o)                  | c1ccccc1            | Benzene (C₆H₆)                   |
| Charge               | + or - in brackets [ ]                       | [C+]                | Carbocation (e.g., CH₃⁺)         |
| Explicit Hydrogen    | [H] or attached in brackets                  | C[NH2]              | Methylamine (CH₃-NH₂)            |
| Functional Group     | Combined atoms (e.g., =O, OH)                | C(=O)O              | Formic Acid (HCOOH)              |
| Stereochemistry      | Slash (/) or backslash (backslash)           | C/C=C/C             | Trans-2-butene (CH₃-CH=CH-CH₃)   |
| Special Bond (Rare)  | Colon (:) for unusual bonds                  | C: (conceptual)     | Carbene (simplified)             |


We have many functinal group the table would be like
| Name                      | SMILES Example(s)          | Formula                  | Key Feature                        |
|---------------------------|----------------------------|--------------------------|------------------------------------|
| Alkane                    | C, CCCCC                   | CnH2n+2                  | Single C-C bonds                   |
| Alkene                    | C=C, CCCC=C                | R-CH=CH2                 | C=C double bond (terminal)         |
| Alkene (internal)         | CC=CCC                     | R-CH=CH-R'               | C=C double bond (internal)         |
| Alkyne                    | C#C, CCCC#C                | R-C≡CH                   | C≡C triple bond (terminal)         |
| Alkyne (internal)         | CC#CCC                     | R-C≡C-R'                 | C≡C triple bond (internal)         |
| Alcohol                   | CO, CCCCO                  | R-OH                     | -OH hydroxyl group                 |
| Aldehyde                  | C=O, CCCC=O                | R-CHO                    | -CHO carbonyl group                |
| Ketone                    | CCC(=O)C, CCCCC(=O)CC      | R-CO-R'                  | >C=O carbonyl within chain         |
| Carboxylic Acid           | C(=O)O, CCCC(=O)O          | R-COOH                   | -COOH carboxyl group               |
| Ester                     | CC(=O)OC, CCCC(=O)OCC      | R-COO-R'                 | -COOR ester linkage                |
| Ether                     | COC, CCCOCC                | R-O-R'                   | R-O-R oxygen bridge                |
| Amine (primary)           | CN, CCCCN                  | R-NH2                    | -NH2 amino group                   |
| Amine (secondary)         | CNC, CCCNCC                | R-NH-R'                  | -NHR secondary amine               |
| Amide                     | CC(=O)N, CCCC(=O)NC        | R-CONH2                  | -CONH2 amide linkage               |
| Halide                    | CF, CCCCl                  | R-X (X=F,Cl,Br,I)        | -X halogen substituent             |
| Nitrile                   | CC#N, CCCC#N               | R-C≡N                    | -C≡N triple bond                   |
| Thiol                     | CS, CCCCS                  | R-SH                     | -SH sulfhydryl group               |
| Sulfide                   | CSC, CCCSCC                | R-S-R'                   | R-S-R sulfur bridge                |
| Allene                    | C=C=C, CCCC=C=C            | R-C=C=CH2                | C=C=C cumulated double bonds       |
| Allene (internal)         | CC=C=CC                    | R-C=C=C-R'               | C=C=C cumulated (internal)         |
| Cycloalkane               | C1CC1, C1CCCCC1            | CnH2n                    | Saturated ring                     |
| Heterocycle (O)           | C1CO1, C1CCCO1             | Cn-1H2n-2O               | Ring with oxygen                   |
| Heterocycle (N)           | C1CN1, C1CCCN1             | Cn-1H2n-1N               | Ring with nitrogen                 |
| Cumulene                  | C=C=C=C, CCCC=C=C=C        | R-C=C=C=CH2              | Three+ consecutive double bonds    |
| Cumulene (internal)       | CC=C=C=CC                  | R-C=C=C=C-R'             | Internal cumulene                  |
| Aromatic                  | c1ccccc1                   | CnHn-6 (e.g., benzene)   | Delocalized π electrons            |
| Bridged Bicyclic          | C1CC2CCC1C2                | CnH2n-2                  | Two rings with a bridge            |
| Spiro                     | C1CCC2(C1)CCCC2            | CnH2n-2                  | Two rings, one shared atom         |
| Cage                      | C12CC3CC(C1)CC(C2)C3       | CnHn-2 (e.g., cubane)    | Polycyclic cage structure          |
| Carbene (Stabilized)      | c1[nH]c(c(c1)NC)NC         | R2C: (e.g., NHC)         | Divalent carbon, stabilized        |
| Strained Small Ring       | C1C=C1                     | CnH2n-2 (e.g., cyclopropene) | High strain, small ring        |
| Macrocycle                | C1CCCCCC1                  | CnH2n                    | Large saturated ring               |
| Polyyne                   | C#CC#C, CCCC#CC#C          | R-C≡C-C≡CH               | Consecutive triple bonds           |
| Non-Classical Carbocation | CC(C)(C)[C+]               | R3C+ (e.g., norbornyl)   | Delocalized positive charge        |
| Borane/Carborane          | B1C2CC1C2                  | CnBmHk (e.g., C2B10H12)  | Three-center two-electron bonds    |
| Möbius Aromatic           | c1ccccccc1                 | CnHn (twisted)           | Twisted π system                   |
| Benzyne                   | c1cccc#c1                  | C6H4                     | Strained "triple bond" in ring     |
| Anti-Aromatic             | C1=CC=C1                   | CnHn (e.g., C4H4)        | 4n π electrons, unstable           |
| Phosphorus Ylide          | C=P(C)(C)C                 | R3P=CH2                  | Polarized C=P bond                 |
| Silylene                  | C[Si]C                     | R2Si:                    | Divalent silicon                   |

# Caption: Organic Molecules with Unique Bonding Structures and Functional Groups.
# Near to 400 molecules and 1000 timesteps per each. If we consider benzene as a base
# and add other groups to benzene, it could raise to 600.

"""


formula_range_pairs = [
    ("CnH2n+2", 1, 12),              # Alkane
    ("R-CH=CH2", 2, 12),             # Alkene
    # ("R-CH=CH-R'", 4, 12),           # Alkene (internal)
    # ("R-C≡CH", 2, 12),               # Alkyne
    # ("R-C≡C-R'", 4, 12),             # Alkyne (internal)
    # ("R-OH", 1, 12),                 # Alcohol
    # ("R-CHO", 1, 12),                # Aldehyde
    # ("R-CO-R'", 3, 12),              # Ketone
    # ("R-COOH", 1, 12),               # Carboxylic Acid
    # ("R-COO-R'", 2, 12),             # Ester
    # ("R-O-R'", 2, 12),               # Ether
    # ("R-NH2", 1, 12),                # Amine (primary)
    # ("R-NH-R'", 2, 12),              # Amine (secondary)
    # ("R-CONH2", 2, 12),              # Amide
    # ("R-X (X=F,Cl,Br,I)", 1, 12),    # Halide
    # ("R-C≡N", 2, 12),                # Nitrile
    # ("R-SH", 1, 12),                 # Thiol
    # ("R-S-R'", 2, 12),               # Sulfide
    # ("R-C=C=CH2", 3, 12),            # Allene
    # ("R-C=C=C-R'", 5, 12),           # Allene (internal)
    # ("CnH2n", 3, 12),                # Cycloalkane
    # ("Cn-1H2n-2O", 2, 12),           # Heterocycle (O)
    # ("Cn-1H2n-1N", 2, 12),           # Heterocycle (N)
    # ("R-C=C=C=CH2", 4, 12),          # Cumulene
    # ("R-C=C=C=C-R'", 6, 12),         # Cumulene (internal)
    # ("CnHn-6 (e.g., benzene)", 6, 12), # Aromatic
    # ("CnH2n-2", 6, 12),              # Bridged Bicyclic
    # ("CnH2n-2", 6, 12),              # Spiro
    # ("CnHn-2 (e.g., cubane)", 6, 12), # Cage
    # ("R2C: (e.g., NHC)", 3, 12),     # Carbene (Stabilized)
    # ("CnH2n-2 (e.g., cyclopropene)", 3, 6), # Strained Small Ring
    # ("CnH2n", 6, 12),                # Macrocycle
    # ("R-C≡C-C≡CH", 4, 12),           # Polyyne
    # ("R3C+ (e.g., norbornyl)", 4, 12), # Non-Classical Carbocation
    # ("CnBmHk (e.g., C2B10H12)", 2, 12), # Borane/Carborane
    # ("CnHn (twisted)", 8, 12),       # Möbius Aromatic
    # ("C6H4", 6, 6),                     # Benzyne
    # ("CnHn (e.g., C4H4)", 4, 8),     # Anti-Aromatic
    # ("R3P=CH2", 2, 12),              # Phosphorus Ylide
    # ("R2Si:", 2, 12)                 # Silylene
]

def chain_generator(semi_smile_format: str, min_chain_length: int, max_chain_length: int):
    molecules = ()
    core = semi_smile_format.split("R")
    if min_chain_length == max_chain_length:
        return molecules
    return chain_generator()


chain_generator(
    formula_range_pairs[0][0],
    formula_range_pairs[0][1],
    formula_range_pairs[0][2]
)