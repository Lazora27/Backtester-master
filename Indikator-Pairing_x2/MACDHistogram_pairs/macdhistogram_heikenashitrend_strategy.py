import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
