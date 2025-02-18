import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und TrueRange
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'TrueRange': 1.0
        })
    )
