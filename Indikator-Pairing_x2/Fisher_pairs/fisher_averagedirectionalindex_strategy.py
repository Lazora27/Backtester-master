import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
