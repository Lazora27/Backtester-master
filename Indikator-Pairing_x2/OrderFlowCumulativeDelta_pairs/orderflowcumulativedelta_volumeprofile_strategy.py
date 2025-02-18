import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderFlowCumulativeDelta_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderFlowCumulativeDelta und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'OrderFlowCumulativeDelta': {
                'class': OrderFlowCumulativeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderFlowCumulativeDelta'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'OrderFlowCumulativeDelta': 1.0,
            'VolumeProfile': 1.0
        })
    )
