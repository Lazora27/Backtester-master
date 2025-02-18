import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_KDJIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und KDJIndicator
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'KDJIndicator': 1.0
        })
    )
