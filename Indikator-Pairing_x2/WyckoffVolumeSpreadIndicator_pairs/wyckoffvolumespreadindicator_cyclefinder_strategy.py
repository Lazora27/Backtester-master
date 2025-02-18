import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WyckoffVolumeSpreadIndicator_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WyckoffVolumeSpreadIndicator und CycleFinder
    """
    
    params = (
        ('indicators', {
            'WyckoffVolumeSpreadIndicator': {
                'class': WyckoffVolumeSpreadIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WyckoffVolumeSpreadIndicator'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'WyckoffVolumeSpreadIndicator': 1.0,
            'CycleFinder': 1.0
        })
    )
