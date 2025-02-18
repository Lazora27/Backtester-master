import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderFlowCumulativeDelta_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderFlowCumulativeDelta und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'OrderFlowCumulativeDelta': {
                'class': OrderFlowCumulativeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderFlowCumulativeDelta'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'OrderFlowCumulativeDelta': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
