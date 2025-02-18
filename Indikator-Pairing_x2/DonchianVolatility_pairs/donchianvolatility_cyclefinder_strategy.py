import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und CycleFinder
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'CycleFinder': 1.0
        })
    )
