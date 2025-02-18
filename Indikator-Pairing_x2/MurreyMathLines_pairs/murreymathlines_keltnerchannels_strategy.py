import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'KeltnerChannels': 1.0
        })
    )
