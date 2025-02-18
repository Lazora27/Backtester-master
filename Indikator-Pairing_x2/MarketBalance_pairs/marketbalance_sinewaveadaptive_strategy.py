import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
