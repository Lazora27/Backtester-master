import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und BarStrength
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'BarStrength': 1.0
        })
    )
