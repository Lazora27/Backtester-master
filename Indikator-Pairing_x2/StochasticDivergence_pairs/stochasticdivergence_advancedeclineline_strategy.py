import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_AdvanceDeclineLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und AdvanceDeclineLine
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'AdvanceDeclineLine': 1.0
        })
    )
