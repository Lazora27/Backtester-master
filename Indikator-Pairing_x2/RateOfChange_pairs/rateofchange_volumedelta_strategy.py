import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'VolumeDelta': 1.0
        })
    )
