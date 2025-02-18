import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und BarStrength
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'BarStrength': 1.0
        })
    )
