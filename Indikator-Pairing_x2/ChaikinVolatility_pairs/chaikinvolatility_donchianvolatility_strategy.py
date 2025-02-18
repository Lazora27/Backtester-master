import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'DonchianVolatility': 1.0
        })
    )
