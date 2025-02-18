import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
