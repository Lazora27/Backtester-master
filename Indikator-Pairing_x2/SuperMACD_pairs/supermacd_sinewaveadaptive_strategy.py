import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
