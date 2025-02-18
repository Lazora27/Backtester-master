import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
