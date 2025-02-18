import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'GannSquareReversal': 1.0
        })
    )
