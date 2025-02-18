import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'AdaptiveATR': 1.0
        })
    )
