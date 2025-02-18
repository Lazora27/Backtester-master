import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'DonchianChannels': 1.0
        })
    )
