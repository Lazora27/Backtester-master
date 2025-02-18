import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
