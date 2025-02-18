import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
