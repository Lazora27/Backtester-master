import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'DonchianChannels': 1.0
        })
    )
