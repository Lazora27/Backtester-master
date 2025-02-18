import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und BarStrength
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'BarStrength': 1.0
        })
    )
