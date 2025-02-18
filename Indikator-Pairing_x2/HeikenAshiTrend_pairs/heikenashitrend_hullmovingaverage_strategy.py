import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'HullMovingAverage': 1.0
        })
    )
