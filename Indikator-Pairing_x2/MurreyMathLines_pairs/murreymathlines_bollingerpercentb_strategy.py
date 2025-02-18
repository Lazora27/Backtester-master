import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'BollingerPercentB': 1.0
        })
    )
