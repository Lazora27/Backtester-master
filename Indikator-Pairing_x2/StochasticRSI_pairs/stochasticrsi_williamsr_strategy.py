import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und WilliamsR
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'WilliamsR': 1.0
        })
    )
