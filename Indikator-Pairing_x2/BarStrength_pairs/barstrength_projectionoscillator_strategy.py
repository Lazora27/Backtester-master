import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
