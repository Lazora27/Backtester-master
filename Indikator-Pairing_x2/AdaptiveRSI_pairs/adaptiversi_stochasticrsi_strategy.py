import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'StochasticRSI': 1.0
        })
    )
