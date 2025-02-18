import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
