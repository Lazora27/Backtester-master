import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und MovingAverage
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'MovingAverage': 1.0
        })
    )
