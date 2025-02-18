import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
