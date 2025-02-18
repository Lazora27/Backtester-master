import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und PriceDelta
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'PriceDelta': 1.0
        })
    )
