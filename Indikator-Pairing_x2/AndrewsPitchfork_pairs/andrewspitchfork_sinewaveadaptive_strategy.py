import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
