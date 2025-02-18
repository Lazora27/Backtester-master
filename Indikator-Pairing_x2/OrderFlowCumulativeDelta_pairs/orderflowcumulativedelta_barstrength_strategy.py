import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderFlowCumulativeDelta_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderFlowCumulativeDelta und BarStrength
    """
    
    params = (
        ('indicators', {
            'OrderFlowCumulativeDelta': {
                'class': OrderFlowCumulativeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderFlowCumulativeDelta'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'OrderFlowCumulativeDelta': 1.0,
            'BarStrength': 1.0
        })
    )
