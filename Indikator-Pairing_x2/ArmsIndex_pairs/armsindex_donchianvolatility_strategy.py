import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'DonchianVolatility': 1.0
        })
    )
