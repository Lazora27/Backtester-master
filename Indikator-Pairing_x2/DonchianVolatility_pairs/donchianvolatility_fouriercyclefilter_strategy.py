import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
