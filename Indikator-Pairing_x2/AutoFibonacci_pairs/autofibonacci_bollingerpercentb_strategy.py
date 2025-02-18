import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'BollingerPercentB': 1.0
        })
    )
