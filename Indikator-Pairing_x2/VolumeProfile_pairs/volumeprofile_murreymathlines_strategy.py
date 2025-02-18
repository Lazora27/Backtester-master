import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'MurreyMathLines': 1.0
        })
    )
