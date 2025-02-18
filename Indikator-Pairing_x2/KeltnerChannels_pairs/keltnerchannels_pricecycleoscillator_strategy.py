import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
