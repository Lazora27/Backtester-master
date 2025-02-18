import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'BuyingPressure': 1.0
        })
    )
