import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_McClellanSummationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und McClellanSummationIndex
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'McClellanSummationIndex': 1.0
        })
    )
