import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_HighLowDifference_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und HighLowDifference
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'HighLowDifference': 1.0
        })
    )
