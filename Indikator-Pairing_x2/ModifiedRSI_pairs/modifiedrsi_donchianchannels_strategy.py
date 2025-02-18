import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'DonchianChannels': 1.0
        })
    )
