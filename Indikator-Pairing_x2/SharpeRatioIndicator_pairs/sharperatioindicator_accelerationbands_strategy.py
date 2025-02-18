import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SharpeRatioIndicator_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SharpeRatioIndicator und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'SharpeRatioIndicator': 1.0,
            'AccelerationBands': 1.0
        })
    )
