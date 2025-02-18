import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'SmoothedCycle': 1.0
        })
    )
