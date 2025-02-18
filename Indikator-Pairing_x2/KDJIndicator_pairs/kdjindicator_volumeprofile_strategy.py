import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'VolumeProfile': 1.0
        })
    )
