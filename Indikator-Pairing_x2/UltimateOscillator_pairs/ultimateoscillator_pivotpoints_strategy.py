import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und PivotPoints
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'PivotPoints': 1.0
        })
    )
