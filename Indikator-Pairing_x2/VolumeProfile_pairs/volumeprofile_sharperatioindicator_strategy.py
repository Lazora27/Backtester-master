import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
