import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
