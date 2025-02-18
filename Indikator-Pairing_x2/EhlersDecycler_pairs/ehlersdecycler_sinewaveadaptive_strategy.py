import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersDecycler_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersDecycler und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'EhlersDecycler': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
