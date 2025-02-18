import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'DonchianVolatility': 1.0
        })
    )
