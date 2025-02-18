import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_SmoothedVolatilityIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und SmoothedVolatilityIndicator
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'SmoothedVolatilityIndicator': {
                'class': SmoothedVolatilityIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedVolatilityIndicator'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'SmoothedVolatilityIndicator': 1.0
        })
    )
