import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
