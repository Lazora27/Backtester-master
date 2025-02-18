import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_OrderFlowCumulativeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und OrderFlowCumulativeDelta
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'OrderFlowCumulativeDelta': {
                'class': OrderFlowCumulativeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderFlowCumulativeDelta'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'OrderFlowCumulativeDelta': 1.0
        })
    )
