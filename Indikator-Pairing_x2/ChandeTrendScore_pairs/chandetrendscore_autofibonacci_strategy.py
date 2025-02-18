import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'AutoFibonacci': 1.0
        })
    )
