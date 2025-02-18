import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderFlowCumulativeDelta_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderFlowCumulativeDelta und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'OrderFlowCumulativeDelta': {
                'class': OrderFlowCumulativeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderFlowCumulativeDelta'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'OrderFlowCumulativeDelta': 1.0,
            'DonchianChannels': 1.0
        })
    )
