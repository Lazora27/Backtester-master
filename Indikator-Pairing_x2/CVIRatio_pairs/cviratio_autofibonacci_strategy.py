import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'AutoFibonacci': 1.0
        })
    )
