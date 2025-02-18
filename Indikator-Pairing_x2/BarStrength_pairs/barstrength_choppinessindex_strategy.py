import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
