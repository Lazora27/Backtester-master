import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'UlcerIndex': 1.0
        })
    )
