import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WyckoffVolumeSpreadIndicator_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WyckoffVolumeSpreadIndicator und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'WyckoffVolumeSpreadIndicator': {
                'class': WyckoffVolumeSpreadIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WyckoffVolumeSpreadIndicator'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'WyckoffVolumeSpreadIndicator': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
