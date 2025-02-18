import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'KeltnerChannels': 1.0
        })
    )
