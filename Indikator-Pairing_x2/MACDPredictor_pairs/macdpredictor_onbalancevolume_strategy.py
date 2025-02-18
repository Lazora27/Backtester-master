import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
