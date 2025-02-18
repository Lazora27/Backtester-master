import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
