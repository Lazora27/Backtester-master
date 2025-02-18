import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'AutoFibonacci': 1.0
        })
    )
