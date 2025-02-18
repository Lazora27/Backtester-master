import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
