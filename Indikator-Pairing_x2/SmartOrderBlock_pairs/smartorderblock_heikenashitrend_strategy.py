import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
