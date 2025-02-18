import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und TrendCycles
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'TrendCycles': 1.0
        })
    )
