import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und CycleFinder
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'CycleFinder': 1.0
        })
    )
