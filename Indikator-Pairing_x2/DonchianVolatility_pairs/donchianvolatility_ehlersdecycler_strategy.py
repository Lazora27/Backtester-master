import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'EhlersDecycler': 1.0
        })
    )
