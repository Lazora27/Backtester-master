import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'CoppockCurve': 1.0
        })
    )
