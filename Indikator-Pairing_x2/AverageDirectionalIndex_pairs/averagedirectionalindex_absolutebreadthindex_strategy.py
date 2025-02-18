import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_AbsoluteBreadthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und AbsoluteBreadthIndex
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'AbsoluteBreadthIndex': {
                'class': AbsoluteBreadthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AbsoluteBreadthIndex'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'AbsoluteBreadthIndex': 1.0
        })
    )
