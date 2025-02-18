import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und Fisher
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'Fisher': 1.0
        })
    )
