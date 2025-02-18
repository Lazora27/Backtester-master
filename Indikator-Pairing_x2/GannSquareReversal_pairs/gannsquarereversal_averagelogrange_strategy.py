import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'AverageLogRange': 1.0
        })
    )
