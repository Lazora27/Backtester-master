import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'AverageTrueRange': 1.0
        })
    )
