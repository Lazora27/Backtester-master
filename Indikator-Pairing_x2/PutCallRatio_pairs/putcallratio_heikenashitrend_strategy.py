import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
