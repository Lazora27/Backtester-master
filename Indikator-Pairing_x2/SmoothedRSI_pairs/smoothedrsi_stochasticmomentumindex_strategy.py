import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_StochasticMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und StochasticMomentumIndex
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'StochasticMomentumIndex': 1.0
        })
    )
