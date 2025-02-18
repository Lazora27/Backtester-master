import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und TrueRange
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'TrueRange': 1.0
        })
    )
