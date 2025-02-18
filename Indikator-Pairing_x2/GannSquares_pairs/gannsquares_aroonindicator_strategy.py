import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'AroonIndicator': 1.0
        })
    )
