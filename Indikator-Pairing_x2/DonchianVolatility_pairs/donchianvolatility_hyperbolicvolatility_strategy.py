import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
