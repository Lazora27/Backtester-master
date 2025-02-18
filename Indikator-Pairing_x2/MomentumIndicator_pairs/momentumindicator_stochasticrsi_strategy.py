import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'StochasticRSI': 1.0
        })
    )
