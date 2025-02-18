import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
