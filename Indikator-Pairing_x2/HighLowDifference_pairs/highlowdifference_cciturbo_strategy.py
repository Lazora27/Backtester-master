import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und CCITurbo
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'CCITurbo': 1.0
        })
    )
