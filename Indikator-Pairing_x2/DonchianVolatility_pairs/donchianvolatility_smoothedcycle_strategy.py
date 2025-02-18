import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'SmoothedCycle': 1.0
        })
    )
