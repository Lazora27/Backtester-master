import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TradeVolumeIndex_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TradeVolumeIndex und TimeCycle
    """
    
    params = (
        ('indicators', {
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'TradeVolumeIndex': 1.0,
            'TimeCycle': 1.0
        })
    )
