import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaveIndicator_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaveIndicator und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'WolfeWaveIndicator': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
