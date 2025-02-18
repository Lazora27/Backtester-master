import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
