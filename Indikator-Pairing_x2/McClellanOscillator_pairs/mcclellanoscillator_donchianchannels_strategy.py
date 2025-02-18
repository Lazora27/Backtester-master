import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'DonchianChannels': 1.0
        })
    )
