import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
