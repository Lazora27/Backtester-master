import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'AutoFibonacci': 1.0
        })
    )
