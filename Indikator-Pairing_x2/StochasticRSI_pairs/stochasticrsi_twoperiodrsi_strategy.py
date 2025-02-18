import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
