import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'TRIXIndicator': 1.0
        })
    )
