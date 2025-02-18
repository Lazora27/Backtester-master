import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
