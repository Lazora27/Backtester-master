import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
