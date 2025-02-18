import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
