import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und TrueRange
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'TrueRange': 1.0
        })
    )
