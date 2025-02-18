import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_PutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und PutCallRatio
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'PutCallRatio': 1.0
        })
    )
