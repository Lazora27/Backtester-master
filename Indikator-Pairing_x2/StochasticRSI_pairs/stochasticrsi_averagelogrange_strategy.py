import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'AverageLogRange': 1.0
        })
    )
