import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
