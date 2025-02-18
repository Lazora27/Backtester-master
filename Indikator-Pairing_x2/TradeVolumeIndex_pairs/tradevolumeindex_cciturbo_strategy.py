import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TradeVolumeIndex_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TradeVolumeIndex und CCITurbo
    """
    
    params = (
        ('indicators', {
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'TradeVolumeIndex': 1.0,
            'CCITurbo': 1.0
        })
    )
