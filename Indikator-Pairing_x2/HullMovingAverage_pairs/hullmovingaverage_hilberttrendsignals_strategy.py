import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
