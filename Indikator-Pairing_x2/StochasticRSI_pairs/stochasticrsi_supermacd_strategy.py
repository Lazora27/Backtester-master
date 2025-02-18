import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und SuperMACD
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'SuperMACD': 1.0
        })
    )
