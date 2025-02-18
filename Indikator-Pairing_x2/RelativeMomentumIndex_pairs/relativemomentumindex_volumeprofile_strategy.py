import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'VolumeProfile': 1.0
        })
    )
