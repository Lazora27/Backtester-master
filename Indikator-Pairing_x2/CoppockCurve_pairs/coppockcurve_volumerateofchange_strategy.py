import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
