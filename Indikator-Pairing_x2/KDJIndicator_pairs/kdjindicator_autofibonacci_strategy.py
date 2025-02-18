import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'AutoFibonacci': 1.0
        })
    )
