import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und BollingerBands
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'BollingerBands': 1.0
        })
    )
