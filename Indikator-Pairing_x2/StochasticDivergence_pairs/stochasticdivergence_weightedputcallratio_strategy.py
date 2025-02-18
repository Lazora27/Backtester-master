import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_WeightedPutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und WeightedPutCallRatio
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'WeightedPutCallRatio': 1.0
        })
    )
