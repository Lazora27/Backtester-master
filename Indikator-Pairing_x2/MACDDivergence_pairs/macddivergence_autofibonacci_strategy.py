import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'AutoFibonacci': 1.0
        })
    )
