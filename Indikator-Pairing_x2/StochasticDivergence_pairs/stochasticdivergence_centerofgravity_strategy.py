import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'CenterOfGravity': 1.0
        })
    )
