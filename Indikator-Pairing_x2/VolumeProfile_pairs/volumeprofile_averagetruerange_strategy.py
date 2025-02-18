import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'AverageTrueRange': 1.0
        })
    )
