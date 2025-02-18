import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
