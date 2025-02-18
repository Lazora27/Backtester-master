import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'AverageTrueRange': 1.0
        })
    )
