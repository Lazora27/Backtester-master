import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
