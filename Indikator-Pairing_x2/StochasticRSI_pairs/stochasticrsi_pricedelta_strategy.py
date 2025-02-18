import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und PriceDelta
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'PriceDelta': 1.0
        })
    )
