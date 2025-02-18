import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
