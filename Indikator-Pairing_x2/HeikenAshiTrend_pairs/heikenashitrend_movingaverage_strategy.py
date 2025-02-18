import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und MovingAverage
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'MovingAverage': 1.0
        })
    )
