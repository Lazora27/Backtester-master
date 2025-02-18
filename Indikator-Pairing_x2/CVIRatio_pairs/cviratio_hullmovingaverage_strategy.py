import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'HullMovingAverage': 1.0
        })
    )
