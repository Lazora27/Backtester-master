import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
