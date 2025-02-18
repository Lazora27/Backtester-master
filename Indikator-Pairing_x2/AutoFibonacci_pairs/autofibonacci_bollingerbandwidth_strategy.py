import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
