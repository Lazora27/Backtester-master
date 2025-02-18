import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
