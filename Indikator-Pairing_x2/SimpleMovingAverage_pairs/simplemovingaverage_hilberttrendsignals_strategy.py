import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
