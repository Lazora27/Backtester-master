import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'HullMovingAverage': 1.0
        })
    )
