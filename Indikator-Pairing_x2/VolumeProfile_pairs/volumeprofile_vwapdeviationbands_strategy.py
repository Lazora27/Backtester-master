import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
