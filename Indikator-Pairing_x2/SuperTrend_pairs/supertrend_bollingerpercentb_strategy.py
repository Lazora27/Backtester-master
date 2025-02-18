import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'BollingerPercentB': 1.0
        })
    )
