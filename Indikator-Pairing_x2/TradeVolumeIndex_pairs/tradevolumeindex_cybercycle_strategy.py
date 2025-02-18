import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TradeVolumeIndex_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TradeVolumeIndex und CyberCycle
    """
    
    params = (
        ('indicators', {
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'TradeVolumeIndex': 1.0,
            'CyberCycle': 1.0
        })
    )
