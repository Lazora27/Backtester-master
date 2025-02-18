import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_OrderFlowCumulativeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und OrderFlowCumulativeDelta
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'OrderFlowCumulativeDelta': {
                'class': OrderFlowCumulativeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderFlowCumulativeDelta'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'OrderFlowCumulativeDelta': 1.0
        })
    )
