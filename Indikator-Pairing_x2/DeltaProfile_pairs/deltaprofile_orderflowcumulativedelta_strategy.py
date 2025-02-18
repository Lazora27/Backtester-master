import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_OrderFlowCumulativeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und OrderFlowCumulativeDelta
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'OrderFlowCumulativeDelta': {
                'class': OrderFlowCumulativeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderFlowCumulativeDelta'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'OrderFlowCumulativeDelta': 1.0
        })
    )
