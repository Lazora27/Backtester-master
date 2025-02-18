import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'WeightedCycle': 1.0
        })
    )
