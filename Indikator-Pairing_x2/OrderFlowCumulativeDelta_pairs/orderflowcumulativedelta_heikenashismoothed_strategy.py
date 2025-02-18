import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderFlowCumulativeDelta_HeikenAshiSmoothed_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderFlowCumulativeDelta und HeikenAshiSmoothed
    """
    
    params = (
        ('indicators', {
            'OrderFlowCumulativeDelta': {
                'class': OrderFlowCumulativeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderFlowCumulativeDelta'>
            },
            'HeikenAshiSmoothed': {
                'class': HeikenAshiSmoothed,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiSmoothed'>
            }
        }),
        ('weights', {
            'OrderFlowCumulativeDelta': 1.0,
            'HeikenAshiSmoothed': 1.0
        })
    )
