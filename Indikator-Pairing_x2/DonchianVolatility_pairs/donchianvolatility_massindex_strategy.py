import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und MassIndex
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'MassIndex': 1.0
        })
    )
