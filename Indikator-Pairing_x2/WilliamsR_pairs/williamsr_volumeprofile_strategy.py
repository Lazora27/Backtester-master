import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'VolumeProfile': 1.0
        })
    )
