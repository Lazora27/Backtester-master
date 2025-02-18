import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'UlcerIndex': 1.0
        })
    )
