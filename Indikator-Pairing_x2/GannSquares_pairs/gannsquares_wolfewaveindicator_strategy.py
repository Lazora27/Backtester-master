import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
