import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_PutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und PutCallRatio
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'PutCallRatio': 1.0
        })
    )
