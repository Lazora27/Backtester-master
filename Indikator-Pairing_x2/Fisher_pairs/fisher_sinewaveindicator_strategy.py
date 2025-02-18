import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
