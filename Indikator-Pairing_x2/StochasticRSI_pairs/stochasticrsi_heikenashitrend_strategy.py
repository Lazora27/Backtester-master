import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
