import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'BollingerPercentB': 1.0
        })
    )
