import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SharpeRatioIndicator_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SharpeRatioIndicator und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'SharpeRatioIndicator': 1.0,
            'EhlersDecycler': 1.0
        })
    )
