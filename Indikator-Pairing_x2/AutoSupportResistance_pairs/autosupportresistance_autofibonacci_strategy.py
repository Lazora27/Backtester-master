import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'AutoFibonacci': 1.0
        })
    )
