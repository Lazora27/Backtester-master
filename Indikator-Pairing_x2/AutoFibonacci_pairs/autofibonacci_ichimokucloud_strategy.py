import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'IchimokuCloud': 1.0
        })
    )
