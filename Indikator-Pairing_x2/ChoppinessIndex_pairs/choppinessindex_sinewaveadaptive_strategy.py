import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChoppinessIndex_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChoppinessIndex und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'ChoppinessIndex': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
