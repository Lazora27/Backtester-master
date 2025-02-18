import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
