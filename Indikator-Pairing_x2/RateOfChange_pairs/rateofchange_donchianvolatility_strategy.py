import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'DonchianVolatility': 1.0
        })
    )
