import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'AutoFibonacci': 1.0
        })
    )
