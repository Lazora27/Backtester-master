import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
