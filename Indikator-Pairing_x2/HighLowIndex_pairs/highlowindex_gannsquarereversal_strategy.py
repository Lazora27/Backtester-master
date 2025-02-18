import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'GannSquareReversal': 1.0
        })
    )
