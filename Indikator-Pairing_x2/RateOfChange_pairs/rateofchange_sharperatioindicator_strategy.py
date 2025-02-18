import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
