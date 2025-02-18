import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'AutoFibonacci': 1.0
        })
    )
