import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersFisherTransform_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersFisherTransform und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'EhlersFisherTransform': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
