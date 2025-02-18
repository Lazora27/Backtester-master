import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
