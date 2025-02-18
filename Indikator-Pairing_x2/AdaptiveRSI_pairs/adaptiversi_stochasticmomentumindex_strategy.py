import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_StochasticMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und StochasticMomentumIndex
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'StochasticMomentumIndex': 1.0
        })
    )
