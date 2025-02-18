import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
