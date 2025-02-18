import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'ProjectionBands': 1.0
        })
    )
