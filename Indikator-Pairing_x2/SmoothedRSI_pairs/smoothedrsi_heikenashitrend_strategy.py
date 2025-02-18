import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
