import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und PivotPoints
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'PivotPoints': 1.0
        })
    )
