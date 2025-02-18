import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
