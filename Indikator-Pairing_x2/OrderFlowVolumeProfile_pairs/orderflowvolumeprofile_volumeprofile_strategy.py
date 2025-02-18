import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderFlowVolumeProfile_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderFlowVolumeProfile und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'OrderFlowVolumeProfile': {
                'class': OrderFlowVolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderFlowVolumeProfile'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'OrderFlowVolumeProfile': 1.0,
            'VolumeProfile': 1.0
        })
    )
