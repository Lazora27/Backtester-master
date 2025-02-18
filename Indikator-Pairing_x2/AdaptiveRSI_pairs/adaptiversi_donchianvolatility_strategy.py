import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'DonchianVolatility': 1.0
        })
    )
