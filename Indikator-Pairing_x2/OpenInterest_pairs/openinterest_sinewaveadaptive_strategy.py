import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
