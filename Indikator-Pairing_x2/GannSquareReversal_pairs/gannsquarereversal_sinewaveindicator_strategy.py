import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
