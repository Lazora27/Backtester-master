import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
