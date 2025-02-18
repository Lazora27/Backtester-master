import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
