import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
