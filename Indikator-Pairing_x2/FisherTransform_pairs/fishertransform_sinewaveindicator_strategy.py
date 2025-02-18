import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
