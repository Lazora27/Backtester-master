import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_AdaptiveRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und AdaptiveRSI
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'AdaptiveRSI': 1.0
        })
    )
