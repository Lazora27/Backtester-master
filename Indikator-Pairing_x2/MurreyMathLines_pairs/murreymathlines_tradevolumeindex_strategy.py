import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
