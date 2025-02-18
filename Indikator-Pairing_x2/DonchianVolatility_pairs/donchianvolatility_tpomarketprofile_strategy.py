import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
