import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
