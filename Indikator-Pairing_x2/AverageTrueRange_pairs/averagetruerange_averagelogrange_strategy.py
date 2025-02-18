import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'AverageLogRange': 1.0
        })
    )
