import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und CCITurbo
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'CCITurbo': 1.0
        })
    )
