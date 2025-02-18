import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
