import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'GannSquareReversal': 1.0
        })
    )
