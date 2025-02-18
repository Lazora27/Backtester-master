import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'DonchianVolatility': 1.0
        })
    )
