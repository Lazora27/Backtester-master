import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
