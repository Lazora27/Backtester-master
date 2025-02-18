import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
