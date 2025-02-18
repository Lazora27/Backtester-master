import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'AccelerationBands': 1.0
        })
    )
