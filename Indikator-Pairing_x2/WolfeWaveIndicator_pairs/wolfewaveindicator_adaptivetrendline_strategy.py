import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaveIndicator_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaveIndicator und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'WolfeWaveIndicator': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
