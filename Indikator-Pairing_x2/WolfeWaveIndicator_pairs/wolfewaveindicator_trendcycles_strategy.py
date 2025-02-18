import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaveIndicator_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaveIndicator und TrendCycles
    """
    
    params = (
        ('indicators', {
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'WolfeWaveIndicator': 1.0,
            'TrendCycles': 1.0
        })
    )
