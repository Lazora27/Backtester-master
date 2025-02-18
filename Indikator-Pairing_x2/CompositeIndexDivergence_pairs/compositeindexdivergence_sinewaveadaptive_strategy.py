import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
