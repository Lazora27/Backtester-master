import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
