import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'KeltnerChannels': 1.0
        })
    )
