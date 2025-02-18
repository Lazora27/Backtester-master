import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'SmoothedCycle': 1.0
        })
    )
