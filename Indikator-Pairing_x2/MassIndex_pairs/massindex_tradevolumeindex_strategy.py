import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MassIndex_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MassIndex und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'MassIndex': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
