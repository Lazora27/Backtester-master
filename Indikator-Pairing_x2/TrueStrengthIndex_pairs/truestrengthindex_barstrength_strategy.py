import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und BarStrength
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'BarStrength': 1.0
        })
    )
