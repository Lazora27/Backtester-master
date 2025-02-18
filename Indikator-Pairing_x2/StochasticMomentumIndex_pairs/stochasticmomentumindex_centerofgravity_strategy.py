import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'CenterOfGravity': 1.0
        })
    )
