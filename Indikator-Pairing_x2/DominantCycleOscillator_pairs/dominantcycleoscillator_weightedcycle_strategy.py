import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DominantCycleOscillator_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DominantCycleOscillator und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'DominantCycleOscillator': 1.0,
            'WeightedCycle': 1.0
        })
    )
