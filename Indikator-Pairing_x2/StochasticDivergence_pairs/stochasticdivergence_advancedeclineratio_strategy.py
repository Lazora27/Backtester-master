import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_AdvanceDeclineRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und AdvanceDeclineRatio
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'AdvanceDeclineRatio': {
                'class': AdvanceDeclineRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineRatio'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'AdvanceDeclineRatio': 1.0
        })
    )
