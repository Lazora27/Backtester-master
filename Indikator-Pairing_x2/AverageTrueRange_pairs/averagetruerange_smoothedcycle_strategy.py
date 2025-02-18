import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'SmoothedCycle': 1.0
        })
    )
