import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'AverageTrueRange': 1.0
        })
    )
