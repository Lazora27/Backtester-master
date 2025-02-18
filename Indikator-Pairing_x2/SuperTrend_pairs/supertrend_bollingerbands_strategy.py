import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und BollingerBands
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'BollingerBands': 1.0
        })
    )
