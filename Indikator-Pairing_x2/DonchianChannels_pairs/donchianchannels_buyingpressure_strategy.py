import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'BuyingPressure': 1.0
        })
    )
