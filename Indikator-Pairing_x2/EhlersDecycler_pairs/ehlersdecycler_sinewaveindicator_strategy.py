import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersDecycler_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersDecycler und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'EhlersDecycler': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
