import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
