import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'AutoFibonacci': 1.0
        })
    )
