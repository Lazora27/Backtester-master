import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
