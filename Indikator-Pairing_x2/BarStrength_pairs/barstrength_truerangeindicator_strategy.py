import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
