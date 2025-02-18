import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_DynamicMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und DynamicMomentumIndex
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'DynamicMomentumIndex': 1.0
        })
    )
