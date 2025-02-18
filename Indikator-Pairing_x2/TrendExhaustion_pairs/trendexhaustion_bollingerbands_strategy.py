import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und BollingerBands
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'BollingerBands': 1.0
        })
    )
