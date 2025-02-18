import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
