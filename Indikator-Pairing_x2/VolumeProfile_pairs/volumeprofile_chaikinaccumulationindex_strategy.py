import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_ChaikinAccumulationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und ChaikinAccumulationIndex
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'ChaikinAccumulationIndex': {
                'class': ChaikinAccumulationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinAccumulationIndex'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'ChaikinAccumulationIndex': 1.0
        })
    )
