import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'DonchianVolatility': 1.0
        })
    )
