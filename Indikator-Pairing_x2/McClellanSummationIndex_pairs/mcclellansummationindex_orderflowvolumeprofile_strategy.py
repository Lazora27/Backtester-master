import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_OrderFlowVolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und OrderFlowVolumeProfile
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'OrderFlowVolumeProfile': {
                'class': OrderFlowVolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderFlowVolumeProfile'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'OrderFlowVolumeProfile': 1.0
        })
    )
