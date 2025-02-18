import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
