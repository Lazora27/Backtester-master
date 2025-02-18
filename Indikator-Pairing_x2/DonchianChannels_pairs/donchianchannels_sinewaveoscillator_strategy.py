import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
