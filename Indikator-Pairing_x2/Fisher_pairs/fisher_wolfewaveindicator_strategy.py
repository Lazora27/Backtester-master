import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
