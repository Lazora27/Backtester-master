import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'BradleySiderograph': 1.0
        })
    )
