import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SharpeRatioIndicator_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SharpeRatioIndicator und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'SharpeRatioIndicator': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
