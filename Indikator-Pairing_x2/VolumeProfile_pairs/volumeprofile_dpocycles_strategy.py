import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und DPOCycles
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'DPOCycles': 1.0
        })
    )
