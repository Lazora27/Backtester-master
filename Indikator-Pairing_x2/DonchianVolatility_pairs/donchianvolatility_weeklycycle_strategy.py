import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'WeeklyCycle': 1.0
        })
    )
