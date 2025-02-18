import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'DonchianVolatility': 1.0
        })
    )
