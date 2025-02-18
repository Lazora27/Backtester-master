import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'TRIXIndicator': 1.0
        })
    )
