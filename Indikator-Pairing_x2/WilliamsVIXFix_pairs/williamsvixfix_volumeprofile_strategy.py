import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'VolumeProfile': 1.0
        })
    )
