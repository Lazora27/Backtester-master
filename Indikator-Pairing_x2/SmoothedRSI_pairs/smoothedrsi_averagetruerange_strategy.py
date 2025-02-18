import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'AverageTrueRange': 1.0
        })
    )
