import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
