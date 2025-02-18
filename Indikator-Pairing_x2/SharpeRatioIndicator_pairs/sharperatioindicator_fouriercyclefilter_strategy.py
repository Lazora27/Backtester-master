import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SharpeRatioIndicator_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SharpeRatioIndicator und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'SharpeRatioIndicator': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
