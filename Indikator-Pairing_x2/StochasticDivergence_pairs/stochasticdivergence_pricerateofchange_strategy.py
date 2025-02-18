import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
