import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'TRIXIndicator': 1.0
        })
    )
