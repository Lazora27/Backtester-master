import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
