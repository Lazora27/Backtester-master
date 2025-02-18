import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_McClellanSummationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und McClellanSummationIndex
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'McClellanSummationIndex': 1.0
        })
    )
