import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CycleFinder_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CycleFinder und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'CycleFinder': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
