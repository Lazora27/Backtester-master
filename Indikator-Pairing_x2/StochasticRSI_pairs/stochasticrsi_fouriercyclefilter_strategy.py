import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
