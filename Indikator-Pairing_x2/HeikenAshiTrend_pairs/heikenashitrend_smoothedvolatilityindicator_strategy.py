import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_SmoothedVolatilityIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und SmoothedVolatilityIndicator
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'SmoothedVolatilityIndicator': {
                'class': SmoothedVolatilityIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedVolatilityIndicator'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'SmoothedVolatilityIndicator': 1.0
        })
    )
