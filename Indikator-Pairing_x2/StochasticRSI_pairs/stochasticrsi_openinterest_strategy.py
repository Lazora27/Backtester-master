import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und OpenInterest
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'OpenInterest': 1.0
        })
    )
