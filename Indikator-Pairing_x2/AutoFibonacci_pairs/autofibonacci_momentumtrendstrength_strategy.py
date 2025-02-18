import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
