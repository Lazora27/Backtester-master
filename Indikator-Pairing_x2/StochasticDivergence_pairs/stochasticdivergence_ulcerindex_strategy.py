import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'UlcerIndex': 1.0
        })
    )
