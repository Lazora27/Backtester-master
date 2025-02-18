import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'DonchianChannels': 1.0
        })
    )
