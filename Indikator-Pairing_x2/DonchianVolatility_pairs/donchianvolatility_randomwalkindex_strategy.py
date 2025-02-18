import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
