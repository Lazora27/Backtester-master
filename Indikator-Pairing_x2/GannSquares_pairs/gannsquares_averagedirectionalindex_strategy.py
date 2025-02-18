import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
