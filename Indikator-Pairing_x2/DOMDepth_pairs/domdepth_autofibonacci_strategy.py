import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'AutoFibonacci': 1.0
        })
    )
