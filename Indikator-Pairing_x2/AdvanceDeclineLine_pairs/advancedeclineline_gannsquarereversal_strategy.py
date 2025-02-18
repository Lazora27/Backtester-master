import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'GannSquareReversal': 1.0
        })
    )
