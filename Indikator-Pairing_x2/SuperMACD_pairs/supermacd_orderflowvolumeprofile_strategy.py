import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_OrderFlowVolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und OrderFlowVolumeProfile
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'OrderFlowVolumeProfile': {
                'class': OrderFlowVolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderFlowVolumeProfile'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'OrderFlowVolumeProfile': 1.0
        })
    )
