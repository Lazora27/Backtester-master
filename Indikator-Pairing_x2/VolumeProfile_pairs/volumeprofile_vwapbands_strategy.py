import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und VWAPBands
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'VWAPBands': 1.0
        })
    )
