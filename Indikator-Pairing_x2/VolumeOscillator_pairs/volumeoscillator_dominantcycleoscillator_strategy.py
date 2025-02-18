import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeOscillator_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeOscillator und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'VolumeOscillator': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
