import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeVolumeIndex_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeVolumeIndex und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'CumulativeVolumeIndex': {
                'class': CumulativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeVolumeIndex'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'CumulativeVolumeIndex': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
