import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'AutoFibonacci': 1.0
        })
    )
