import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
