import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_AccumulativeSwingIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und AccumulativeSwingIndex
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'AccumulativeSwingIndex': {
                'class': AccumulativeSwingIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulativeSwingIndex'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'AccumulativeSwingIndex': 1.0
        })
    )
