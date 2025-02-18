import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SharpeRatioIndicator_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SharpeRatioIndicator und CycleFinder
    """
    
    params = (
        ('indicators', {
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'SharpeRatioIndicator': 1.0,
            'CycleFinder': 1.0
        })
    )
