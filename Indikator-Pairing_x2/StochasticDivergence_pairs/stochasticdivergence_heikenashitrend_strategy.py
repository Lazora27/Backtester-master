import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
