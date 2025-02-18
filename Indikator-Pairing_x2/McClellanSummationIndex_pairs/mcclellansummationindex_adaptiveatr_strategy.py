import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'AdaptiveATR': 1.0
        })
    )
