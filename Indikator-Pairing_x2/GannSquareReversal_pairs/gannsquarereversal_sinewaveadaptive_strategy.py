import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
