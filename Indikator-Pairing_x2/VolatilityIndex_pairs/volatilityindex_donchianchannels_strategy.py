import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'DonchianChannels': 1.0
        })
    )
