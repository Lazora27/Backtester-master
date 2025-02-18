import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und DPOCycles
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'DPOCycles': 1.0
        })
    )
