import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
