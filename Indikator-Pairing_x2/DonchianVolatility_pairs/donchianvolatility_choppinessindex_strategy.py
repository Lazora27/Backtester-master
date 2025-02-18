import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
