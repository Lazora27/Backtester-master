import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und BarStrength
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'BarStrength': 1.0
        })
    )
