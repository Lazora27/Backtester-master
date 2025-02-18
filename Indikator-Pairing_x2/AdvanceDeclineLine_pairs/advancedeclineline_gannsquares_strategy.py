import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und GannSquares
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'GannSquares': 1.0
        })
    )
