import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'AverageTrueRange': 1.0
        })
    )
