import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
