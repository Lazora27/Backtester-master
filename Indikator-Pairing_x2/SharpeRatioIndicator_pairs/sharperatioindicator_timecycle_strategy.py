import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SharpeRatioIndicator_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SharpeRatioIndicator und TimeCycle
    """
    
    params = (
        ('indicators', {
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'SharpeRatioIndicator': 1.0,
            'TimeCycle': 1.0
        })
    )
