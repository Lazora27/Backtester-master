import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
