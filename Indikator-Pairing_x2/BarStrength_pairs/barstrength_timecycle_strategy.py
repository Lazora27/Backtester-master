import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und TimeCycle
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'TimeCycle': 1.0
        })
    )
