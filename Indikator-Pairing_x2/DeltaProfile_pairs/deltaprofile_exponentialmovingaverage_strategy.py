import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
