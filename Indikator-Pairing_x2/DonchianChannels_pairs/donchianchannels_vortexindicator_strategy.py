import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'VortexIndicator': 1.0
        })
    )
