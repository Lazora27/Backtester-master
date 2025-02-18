import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'DonchianVolatility': 1.0
        })
    )
