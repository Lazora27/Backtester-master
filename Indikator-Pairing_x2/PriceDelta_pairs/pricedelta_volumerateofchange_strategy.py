import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
