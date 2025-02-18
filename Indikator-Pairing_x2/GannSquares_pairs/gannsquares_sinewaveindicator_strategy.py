import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
