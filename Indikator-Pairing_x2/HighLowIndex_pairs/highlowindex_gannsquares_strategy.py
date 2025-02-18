import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und GannSquares
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'GannSquares': 1.0
        })
    )
