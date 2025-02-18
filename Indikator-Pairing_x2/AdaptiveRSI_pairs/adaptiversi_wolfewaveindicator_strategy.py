import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
