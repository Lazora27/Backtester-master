import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_UltimateOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und UltimateOscillator
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'UltimateOscillator': 1.0
        })
    )
