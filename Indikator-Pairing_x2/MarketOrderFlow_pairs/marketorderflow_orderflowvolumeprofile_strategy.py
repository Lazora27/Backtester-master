import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_OrderFlowVolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und OrderFlowVolumeProfile
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'OrderFlowVolumeProfile': {
                'class': OrderFlowVolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderFlowVolumeProfile'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'OrderFlowVolumeProfile': 1.0
        })
    )
