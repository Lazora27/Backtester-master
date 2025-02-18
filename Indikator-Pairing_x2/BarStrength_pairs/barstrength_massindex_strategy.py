import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und MassIndex
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'MassIndex': 1.0
        })
    )
