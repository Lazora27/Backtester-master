import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
