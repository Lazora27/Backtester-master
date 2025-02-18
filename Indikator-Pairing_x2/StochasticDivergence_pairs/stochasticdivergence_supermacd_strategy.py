import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und SuperMACD
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'SuperMACD': 1.0
        })
    )
