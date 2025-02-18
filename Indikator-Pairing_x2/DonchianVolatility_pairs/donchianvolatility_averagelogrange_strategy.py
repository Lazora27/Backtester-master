import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'AverageLogRange': 1.0
        })
    )
