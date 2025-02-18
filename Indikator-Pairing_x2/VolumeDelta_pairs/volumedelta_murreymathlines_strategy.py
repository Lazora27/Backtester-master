import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'MurreyMathLines': 1.0
        })
    )
