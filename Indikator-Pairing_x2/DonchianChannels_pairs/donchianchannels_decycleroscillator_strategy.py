import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
