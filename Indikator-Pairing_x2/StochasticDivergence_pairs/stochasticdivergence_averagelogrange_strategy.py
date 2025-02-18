import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'AverageLogRange': 1.0
        })
    )
