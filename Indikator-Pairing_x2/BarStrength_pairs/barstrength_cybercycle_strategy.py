import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und CyberCycle
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'CyberCycle': 1.0
        })
    )
