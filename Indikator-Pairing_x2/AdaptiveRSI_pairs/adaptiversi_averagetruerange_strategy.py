import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'AverageTrueRange': 1.0
        })
    )
