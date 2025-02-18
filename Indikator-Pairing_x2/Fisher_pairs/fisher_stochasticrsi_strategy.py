import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'StochasticRSI': 1.0
        })
    )
