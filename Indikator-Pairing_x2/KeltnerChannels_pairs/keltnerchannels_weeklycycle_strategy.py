import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'WeeklyCycle': 1.0
        })
    )
