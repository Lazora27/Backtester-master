import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
