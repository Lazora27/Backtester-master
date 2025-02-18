import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'DonchianChannels': 1.0
        })
    )
