import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'AverageTrueRange': 1.0
        })
    )
