import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'AccelerationBands': 1.0
        })
    )
