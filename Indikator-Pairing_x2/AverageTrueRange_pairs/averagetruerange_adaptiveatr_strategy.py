import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'AdaptiveATR': 1.0
        })
    )
