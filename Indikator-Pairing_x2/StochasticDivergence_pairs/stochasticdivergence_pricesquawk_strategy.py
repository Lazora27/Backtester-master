import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'PriceSquawk': 1.0
        })
    )
