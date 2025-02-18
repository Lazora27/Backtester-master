import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
