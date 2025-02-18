import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_OrderFlowCumulativeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und OrderFlowCumulativeDelta
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'OrderFlowCumulativeDelta': {
                'class': OrderFlowCumulativeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderFlowCumulativeDelta'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'OrderFlowCumulativeDelta': 1.0
        })
    )
