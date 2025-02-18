import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_HighLowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und HighLowIndex
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'HighLowIndex': 1.0
        })
    )
