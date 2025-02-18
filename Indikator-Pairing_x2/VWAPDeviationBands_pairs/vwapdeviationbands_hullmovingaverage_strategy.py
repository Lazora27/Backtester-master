import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'HullMovingAverage': 1.0
        })
    )
