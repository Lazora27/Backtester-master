import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'PriceSquawk': 1.0
        })
    )
