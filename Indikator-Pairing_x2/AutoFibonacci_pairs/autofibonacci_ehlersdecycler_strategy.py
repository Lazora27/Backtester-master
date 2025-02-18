import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'EhlersDecycler': 1.0
        })
    )
