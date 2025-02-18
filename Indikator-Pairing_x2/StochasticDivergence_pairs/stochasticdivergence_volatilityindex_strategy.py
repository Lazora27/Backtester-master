import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'VolatilityIndex': 1.0
        })
    )
