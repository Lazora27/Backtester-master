import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und SuperTrend
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'SuperTrend': 1.0
        })
    )
