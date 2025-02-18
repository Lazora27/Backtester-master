import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'AroonIndicator': 1.0
        })
    )
