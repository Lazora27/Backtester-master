import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'DonchianChannels': 1.0
        })
    )
