import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_WyckoffVolumeSpreadIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und WyckoffVolumeSpreadIndicator
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'WyckoffVolumeSpreadIndicator': {
                'class': WyckoffVolumeSpreadIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WyckoffVolumeSpreadIndicator'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'WyckoffVolumeSpreadIndicator': 1.0
        })
    )
