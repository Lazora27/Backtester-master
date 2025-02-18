import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und CCITurbo
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'CCITurbo': 1.0
        })
    )
