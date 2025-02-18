import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'SmoothedRSI': 1.0
        })
    )
