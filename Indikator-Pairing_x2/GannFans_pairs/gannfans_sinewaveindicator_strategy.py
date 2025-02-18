import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
