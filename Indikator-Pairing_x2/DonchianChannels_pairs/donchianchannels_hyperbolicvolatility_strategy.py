import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
