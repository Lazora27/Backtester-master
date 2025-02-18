import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaveIndicator_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaveIndicator und OpenInterest
    """
    
    params = (
        ('indicators', {
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'WolfeWaveIndicator': 1.0,
            'OpenInterest': 1.0
        })
    )
