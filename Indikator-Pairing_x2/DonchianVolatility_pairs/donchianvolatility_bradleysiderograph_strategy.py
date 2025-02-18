import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'BradleySiderograph': 1.0
        })
    )
