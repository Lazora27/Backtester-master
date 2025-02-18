import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
