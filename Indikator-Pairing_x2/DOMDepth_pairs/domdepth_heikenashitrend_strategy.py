import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
