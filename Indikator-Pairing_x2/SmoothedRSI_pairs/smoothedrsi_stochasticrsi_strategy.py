import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'StochasticRSI': 1.0
        })
    )
