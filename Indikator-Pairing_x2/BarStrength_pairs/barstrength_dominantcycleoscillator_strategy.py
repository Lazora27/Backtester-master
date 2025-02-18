import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
