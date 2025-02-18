import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersFisherTransform_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersFisherTransform und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'EhlersFisherTransform': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
