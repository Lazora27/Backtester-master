import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
