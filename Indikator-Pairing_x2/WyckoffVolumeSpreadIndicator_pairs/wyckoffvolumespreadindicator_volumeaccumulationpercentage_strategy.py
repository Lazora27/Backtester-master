import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WyckoffVolumeSpreadIndicator_VolumeAccumulationPercentage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WyckoffVolumeSpreadIndicator und VolumeAccumulationPercentage
    """
    
    params = (
        ('indicators', {
            'WyckoffVolumeSpreadIndicator': {
                'class': WyckoffVolumeSpreadIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WyckoffVolumeSpreadIndicator'>
            },
            'VolumeAccumulationPercentage': {
                'class': VolumeAccumulationPercentage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeAccumulationPercentage'>
            }
        }),
        ('weights', {
            'WyckoffVolumeSpreadIndicator': 1.0,
            'VolumeAccumulationPercentage': 1.0
        })
    )
