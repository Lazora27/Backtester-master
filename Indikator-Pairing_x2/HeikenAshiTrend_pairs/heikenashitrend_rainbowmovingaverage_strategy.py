import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
