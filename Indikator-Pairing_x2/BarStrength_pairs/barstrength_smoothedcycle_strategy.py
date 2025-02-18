import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'SmoothedCycle': 1.0
        })
    )
