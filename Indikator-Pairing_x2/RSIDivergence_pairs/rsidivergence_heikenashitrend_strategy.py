import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
