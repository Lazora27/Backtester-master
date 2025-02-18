import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'ParabolicSAR': 1.0
        })
    )
