import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'HullMovingAverage': 1.0
        })
    )
