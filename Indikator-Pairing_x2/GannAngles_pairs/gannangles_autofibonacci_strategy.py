import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'AutoFibonacci': 1.0
        })
    )
