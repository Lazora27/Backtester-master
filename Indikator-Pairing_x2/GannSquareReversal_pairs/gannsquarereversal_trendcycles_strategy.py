import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und TrendCycles
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'TrendCycles': 1.0
        })
    )
