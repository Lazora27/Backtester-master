import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RoundNumbersIndicator_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RoundNumbersIndicator und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'RoundNumbersIndicator': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
