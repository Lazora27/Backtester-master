import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und TrendCycles
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'TrendCycles': 1.0
        })
    )
