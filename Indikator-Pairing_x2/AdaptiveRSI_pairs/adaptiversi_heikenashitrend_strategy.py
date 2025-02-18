import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
