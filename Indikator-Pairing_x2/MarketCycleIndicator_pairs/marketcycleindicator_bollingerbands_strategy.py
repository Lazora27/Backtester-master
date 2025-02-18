import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und BollingerBands
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'BollingerBands': 1.0
        })
    )
