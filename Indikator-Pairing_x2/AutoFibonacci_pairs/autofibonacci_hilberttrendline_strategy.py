import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'HilbertTrendline': 1.0
        })
    )
