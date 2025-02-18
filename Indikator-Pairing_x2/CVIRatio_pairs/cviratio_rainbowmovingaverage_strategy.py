import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
