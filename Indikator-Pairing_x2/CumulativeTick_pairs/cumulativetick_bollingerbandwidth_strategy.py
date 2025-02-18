import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
