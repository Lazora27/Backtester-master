import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und TrendCycles
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'TrendCycles': 1.0
        })
    )
