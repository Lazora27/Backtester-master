import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'AutoFibonacci': 1.0
        })
    )
