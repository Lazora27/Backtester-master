import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'DonchianChannels': 1.0
        })
    )
