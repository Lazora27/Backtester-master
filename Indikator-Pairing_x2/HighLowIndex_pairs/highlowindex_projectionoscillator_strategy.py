import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
