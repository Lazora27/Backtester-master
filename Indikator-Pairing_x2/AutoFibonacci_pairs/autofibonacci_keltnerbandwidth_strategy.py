import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
