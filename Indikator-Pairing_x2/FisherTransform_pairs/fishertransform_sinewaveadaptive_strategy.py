import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
