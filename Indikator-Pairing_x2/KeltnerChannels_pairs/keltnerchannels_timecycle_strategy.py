import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und TimeCycle
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'TimeCycle': 1.0
        })
    )
