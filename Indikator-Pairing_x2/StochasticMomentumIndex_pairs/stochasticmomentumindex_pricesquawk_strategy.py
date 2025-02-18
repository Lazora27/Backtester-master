import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'PriceSquawk': 1.0
        })
    )
