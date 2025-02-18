import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'AdaptiveATR': 1.0
        })
    )
