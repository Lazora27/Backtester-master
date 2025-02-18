import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
