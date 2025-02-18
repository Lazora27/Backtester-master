import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
