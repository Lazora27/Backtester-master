import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
