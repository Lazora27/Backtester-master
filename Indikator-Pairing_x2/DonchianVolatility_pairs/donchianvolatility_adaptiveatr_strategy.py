import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'AdaptiveATR': 1.0
        })
    )
