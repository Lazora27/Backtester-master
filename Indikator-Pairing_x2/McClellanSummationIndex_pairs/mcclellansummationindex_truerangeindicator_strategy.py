import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
