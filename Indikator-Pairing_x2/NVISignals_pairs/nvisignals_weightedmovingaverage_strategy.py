import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
