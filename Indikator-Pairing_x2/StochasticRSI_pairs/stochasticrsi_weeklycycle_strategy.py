import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'WeeklyCycle': 1.0
        })
    )
