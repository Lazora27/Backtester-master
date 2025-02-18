import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
