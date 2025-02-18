import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderFlowVolumeProfile_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderFlowVolumeProfile und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'OrderFlowVolumeProfile': {
                'class': OrderFlowVolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderFlowVolumeProfile'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'OrderFlowVolumeProfile': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
