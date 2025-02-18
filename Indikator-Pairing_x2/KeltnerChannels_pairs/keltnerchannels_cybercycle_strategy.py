import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und CyberCycle
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'CyberCycle': 1.0
        })
    )
