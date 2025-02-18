import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
