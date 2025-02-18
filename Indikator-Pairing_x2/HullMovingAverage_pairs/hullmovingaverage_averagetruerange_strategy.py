import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'AverageTrueRange': 1.0
        })
    )
