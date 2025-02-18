import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
