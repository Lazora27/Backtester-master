import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und TrueRange
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'TrueRange': 1.0
        })
    )
