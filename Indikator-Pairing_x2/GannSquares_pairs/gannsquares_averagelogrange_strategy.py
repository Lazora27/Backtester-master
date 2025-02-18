import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'AverageLogRange': 1.0
        })
    )
