import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'DonchianChannels': 1.0
        })
    )
